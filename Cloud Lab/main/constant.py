from enum import Enum


class Search(Enum):
    ES_INDEX = "google_files"
    ES_HOST = "http://localhost:9200"
    ES_INDEX_Files = "files"




class Config(Enum):
    ES_HOST = "http://localhost:9200"
