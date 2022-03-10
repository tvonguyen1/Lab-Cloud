from operator import contains

import queries


class search:
    def search(search_text):
        list = search_text.split()
        id = ""
        title = ""
        mime_type = ""
        description = ""
        try:
            for i in list:
                if queries().get_file_id(list[i]):
                    id = id + " " + list[i]
                if queries().get_file_name(list[i]):
                    title = title + " " + list[i]
                if queries().get_file_description(list[i]):
                    description = description + " " + list[i]
        except Exception as ex:
            print('Exception while parsing')
            print(str(ex))


def getfile(service, title, id, description):
    page_token = None
    while True:
        response = service.files().list(q="name contains %s and id contains %s and description contains %s",

                                        spaces='drive',
                                        fields='nextPageToken, files(id, name)',
                                        pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            print
            'Found file: %s (%s)' % (file.get('name'), file.get('id'))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
