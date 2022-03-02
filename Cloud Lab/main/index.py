from tornado.httpclient import HTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
import tornado.options
import json
import time
import calendar
import quopri
import chardet
import ndjson
from bs4 import BeautifulSoup
import logging

http_client = HTTPClient()

DEFAULT_BATCH_SIZE = 500
DEFAULT_ES_URL = "http://localhost:9200"
DEFAULT_INDEX_NAME = "drivefile"


def strip_html_css_js(msg):
    soup = BeautifulSoup(msg, "html.parser")  # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


def delete_index():
    try:
        url = "%s/%s" % (tornado.options.options.es_url, tornado.options.options.index_name)
        request = HTTPRequest(url, method="DELETE", request_timeout=240, headers={"Content-Type": "application/json"})
        response = http_client.fetch(request)
        logging.info('Delete index done   %s' % response.body)
    except:
        pass


def create_index():
    schema = {
        "settings": {
            "number_of_shards": tornado.options.options.num_of_shards,
            "number_of_replicas": 0
        },
        "mappings": {
            "file": {
                "_source": {"enabled": True},
                "properties": {
                    "name": {"type": "string", "index": "not_analyzed"},
                    "type": {"type": "string", "index": "not_analyzed"},
                    "size": {"type": "string", "index": "not_analyzed"},
                    "location": {"type": "string", "index": "not_analyzed"},
                    "file-id": {"type": "string", "index": "not_analyzed"},
                    "owner": {"type": "string", "index": "not_analyzed"},
                    "date_create": {"type": "date"},
                },
            }
        },
        "refresh": True
    }

    body = json.dumps(schema)
    url = "%s/%s" % (tornado.options.options.es_url, tornado.options.options.index_name)
    try:
        request = HTTPRequest(url, method="PUT", body=body, request_timeout=240,
                              headers={"Content-Type": "application/json"})
        response = http_client.fetch(request)
        logging.info('Create index done   %s' % response.body)
    except:
        pass


total_uploaded = 0

def convert_file_to_json(blob):
    json_data_string = blob.download_as_string()
    json_data = ndjson.loads(json_data_string)



def upload_batch(upload_data):
    if tornado.options.options.dry_run:
        logging.info("Dry run, not uploading")
        return
    upload_data_txt = ""
    for item in upload_data:
        cmd = {'index': {'_index': tornado.options.options.index_name, '_type': 'file', '_id': item['message-id']}}
        try:
            json_cmd = json.dumps(cmd) + "\n"
            json_item = json.dumps(item) + "\n"
        except:
            logging.warn('Skipping mail with message id %s because of exception converting to JSON (invalid characters?).' % item['message-id'])
            continue
        upload_data_txt += json_cmd
        upload_data_txt += json_item

    request = HTTPRequest(tornado.options.options.es_url + "/_bulk", method="POST", body=upload_data_txt, request_timeout=240, headers={"Content-Type": "application/json"})
    response = http_client.fetch(request)
    result = json.loads(response.body)

    global total_uploaded
    total_uploaded += len(upload_data)
    res_txt = "OK" if not result['errors'] else "FAILED"
    logging.info("Upload: %s - upload took: %4dms, total messages uploaded: %6d" % (res_txt, result['took'], total_uploaded))
