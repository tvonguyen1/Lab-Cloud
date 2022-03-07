from tornado.httpclient import HTTPClient, HTTPRequest
import tornado.options
import json
import ndjson
from bs4 import BeautifulSoup
import logging
import requests
from elasticsearch import Elasticsearch

http_client = HTTPClient()


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


def search(es_object, index_name, search):
    res = es_object.search(index=index_name, body=search)
    print(res)


def create_index(es_object, index_name):
    created = False
    schema = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "file": {
                "_source": {"enabled": True},
                "properties": {
                    "id": {"type": "string"},
                    "owned_by_me": {"type": "boolean"},
                    "title": {"type": "string"},
                    "type": {"type": "string"},
                    "size": {"type": "string"},
                    "description": {"type": "string"},
                    "date_create": {"type": "datetime"},
                    "labels": {
                        "starred": {"type": "boolean"},
                        "hidden": {"type": "boolean"},
                        "trashed": {"type": "boolean"},
                        "restricted": {"type": "boolean"},
                        "viewed": {"type": "boolean"},
                        "modified": {"type": "boolean"},
                    },
                },
            }
        },
        "refresh": True
    }
    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(index=index_name, ignore=400, body=schema)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


def store_record(elastic_object, index_name, record):
    is_stored = True
    try:
        outcome = elastic_object.index(index=index_name, doc_type='files', body=record)
        print(outcome)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))
        is_stored = False
    finally:
        return is_stored

    def parse(u):
        id = '-'
        owned_by_me = 'false'
        title = '-'
        type = '-'
        size = '-'
        owner = '-'
        date_create = "0001-01-01T00:00:00"
        starred = 'false'
        hidden = 'false'
        trashed = 'false'
        restricted = 'false'
        viewed = 'false'
        modified = 'false'
        rec = {}


def convert_file_to_json(blob):
    json_data_string = blob.download_as_string()
    json_data = ndjson.loads(json_data_string)




