from operator import contains

from drive_connector import connector
from googleapiclient.errors import HttpError


class queries:

    def get_file_name(file_name):
        service = connector()
        try:
            response = service.files().get('name', contains (file_name)).execute()
            return True
        except HttpError as error:
            return False

    def get_file_id(file_id):
        service = connector()
        try:
            response = service.files().get('id', contains(file_id)).execute()
            return True
        except HttpError as error:
            return False

    def get_file_type(mime_type):
        service = connector()
        try:
            response = service.files().get('mimeType', contains (mime_type)).execute()
            return True
        except HttpError as error:
            return False

    def get_file_description(file_description):
        service = connector()
        try:
            response = service.files().get('description', contains (file_description)).execute()
            return True
        except HttpError as error:
            return False





