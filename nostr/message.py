# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.

import json

# TODO::: invalid message, random message and more.

class Message:
    def __init__(self, message_type, data):
        self.message_type = message_type
        self.data = data

    def to_json(self):
        return json.dumps([self.message_type, json.loads(self.data)])

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data[0], data[1])
