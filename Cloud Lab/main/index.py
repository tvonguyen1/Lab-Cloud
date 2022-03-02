from tornado.httpclient import HTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
import tornado.options
import json
import time
import calendar
import quopri
import chardet
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
        request = HTTPRequest(url, method="PUT", body=body, request_timeout=240, headers={"Content-Type": "application/json"})
        response = http_client.fetch(request)
        logging.info('Create index done   %s' % response.body)
    except:
        pass


total_uploaded = 0

