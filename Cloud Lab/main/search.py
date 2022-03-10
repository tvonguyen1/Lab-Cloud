import queries

class search:
    def search (search_text):
        list = search_text.split()
        id = ""
        title = ""
        mime_type = ""
        description = ""
        try:
            for i in list:
                if queries().get_file_id(list[i]):
                    id += list[i]
                if queries().get_file_name(list[i]):
                    title += list[i]
                if queries().get_file_description(list[i]):
                    description += list[i]
        except Exception as ex:
            print('Exception while parsing')
            print(str(ex))



