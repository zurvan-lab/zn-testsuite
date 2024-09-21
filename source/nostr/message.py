# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.
from __future__ import annotations

import json

from .event import Event


class EventToRelayMessage:
    def __init__(self, event: Event) -> None:
        self.event = event

    def to_json(self) -> str:
        return json.dumps(["EVENT", json.loads(self.event.to_json())])

    @classmethod
    def from_json(cls, json_string: str) -> EventToRelayMessage:
        data = json.loads(json_string)
        return cls(data[1])
