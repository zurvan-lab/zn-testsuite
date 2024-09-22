# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.
from __future__ import annotations

import json

from .event import Event
from .filter import Filter


class EventToRelayMessage:
    def __init__(self, event: Event) -> None:
        self.event = event

    def to_json(self) -> str:
        return json.dumps(["EVENT", json.loads(self.event.to_json())])

    @classmethod
    def from_json(cls, json_string: str) -> EventToRelayMessage:
        data = json.loads(json_string)
        return cls(data[1])


class ReqMessage:
    def __init__(self, id: str, filter: Filter) -> None:
        self.id = id
        self.filter = filter

    def to_json(self) -> str:
        return json.dumps(["REQ", self.id, json.loads(self.filter.to_json())])


class EventFromRelayMessage:
    def __init__(self, id: str, event: Event) -> None:
        self.event = event
        self.id = id

    @classmethod
    def from_json(cls, json_string: str) -> EventFromRelayMessage:
        data = json.loads(json_string)
        if len(data) != 3:
            raise Exception("invalid event message, len must be 3!")

        if data[0] != "EVENT":
            raise Exception("invalid event message, index 0 must be EVENT!")

        print(data[2])
        return cls(data[1], data[2])
