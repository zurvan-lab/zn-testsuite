# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.
from __future__ import annotations

import json

from .event import Event


class Message:
    def __init__(self, message_type: str, data: Event) -> None:
        self.message_type = message_type
        self.data = data

    def to_json(self) -> str:
        return json.dumps([self.message_type, json.loads(self.data.to_json())])

    @classmethod
    def from_json(cls, json_string: str) -> Message:
        data = json.loads(json_string)
        return cls(data[0], data[1])
