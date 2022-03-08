from dataclasses import dataclass

import json
import ndjson
from bs4 import BeautifulSoup
from logger import logger
from constant import Search
import requests
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import TransportError, ConnectionError
from queries import queries


@dataclass
class PersonalizedSearch:

    @staticmethod
    def connect_elasticsearch() -> Elasticsearch:
        """
        :return: Elasticsearch client.
        """
        try:
            es_client = Elasticsearch(hosts=Search.ES_HOST)
            return es_client

        except (TransportError, ConnectionError) as exc:
            logger.info(exc, exc_info=True)

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

    def search(es_object, index_name, search):
        res = es_object.search(index=index_name, body=search)
        print(res)

    @staticmethod
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
                        "title": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "description": {"type": "string"},

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

    def parse(search):
        id = '-'
        title = '-'
        mime_type = '-'
        description = '-'
        rec = {}

        list = search.split()
        try:
            for i in list:
                if queries().get_file_id(list[i]):
                    id = list[i]
                if queries().get_file_name(list[i]):
                    title = list[i]
                if queries().get_file_type(list[i]):
                    mime_type = list[i]

                rec = {'id': id, 'title': title, 'mimetype': mime_type, 'description': description}
                json.dumps(rec)
        except Exception as ex:
            print('Exception while parsing')
            print(str(ex))

    def convert_file_to_json(blob):
        json_data_string = blob.download_as_string()
        json_data = ndjson.loads(json_data_string)

    if __name__ == '__main__':

