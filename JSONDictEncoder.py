from json import JSONEncoder


class JSONDictEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__