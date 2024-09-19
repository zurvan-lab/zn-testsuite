# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.

import json

# TODO::: match with event, invalid filter, random filter and more.

class Filter:
    def __init__(self, ids=None, authors=None, kinds=None, tag_filters=None, since=None, until=None, limit=None):
        self.ids = ids or []
        self.authors = authors or []
        self.kinds = kinds or []
        self.tag_filters = tag_filters or {}
        self.since = since
        self.until = until
        self.limit = limit

    def to_json(self):
        filter_dict = {
            "ids": self.ids,
            "authors": self.authors,
            "kinds": self.kinds,
            **self.tag_filters,
            "since": self.since,
            "until": self.until,
            "limit": self.limit
        }
        return json.dumps(filter_dict)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data.get("ids"), data.get("authors"), data.get("kinds"), data.get("tags", {}), data.get("since"), data.get("until"), data.get("limit"))
