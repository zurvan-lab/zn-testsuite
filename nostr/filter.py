# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.
from __future__ import annotations

import json
from typing import Dict, List, Optional

from nostr.event import Event

# TODO::: invalid filter, random filter and more.


class Filter:
    def __init__(
        self,
        ids: Optional[List[str]] = None,
        authors: Optional[List[str]] = None,
        kinds: Optional[List[int]] = None,
        tag_filters: Optional[Dict[str, List[str]]] = None,
        since: int = 0,
        until: int = 0,
        limit: int = 0,
    ) -> None:
        self.ids = ids or []
        self.authors = authors or []
        self.kinds = kinds or []
        self.tag_filters = tag_filters or {}
        self.since = since
        self.until = until
        self.limit = limit

    def to_json(self) -> str:
        filter_dict = {
            "ids": self.ids,
            "authors": self.authors,
            "kinds": self.kinds,
            **self.tag_filters,
            "since": self.since,
            "until": self.until,
            "limit": self.limit,
        }
        return json.dumps(filter_dict)

    def match(self, event: Event) -> bool:
        if Event is None:
            return False

        if len(self.ids) != 0 and not self.ids.__contains__(event.id):
            return False

        if len(self.authors) != 0 and not self.authors.__contains__(event.pubkey):
            return False

        if len(self.kinds) != 0 and not self.kinds.__contains__(event.kind):
            return False

        if self.since != 0 and event.created_at < self.since:
            return False

        if self.until != 0 and event.created_at > self.until:
            return False

        for name, values in self.tag_filters.items():
            has_value = False
            for t in event.tags:
                if len(t) < 2:
                    continue

                if "#" + t[0] == name:
                    for v in values:
                        if v == t[1]:
                            has_value = True
                            break

            if not has_value:
                return False

        return True

    @classmethod
    def from_json(cls, json_string: str) -> Filter:
        data = json.loads(json_string)
        return cls(
            data.get("ids"),
            data.get("authors"),
            data.get("kinds"),
            data.get("tags", {}),
            data.get("since"),
            data.get("until"),
            data.get("limit"),
        )
