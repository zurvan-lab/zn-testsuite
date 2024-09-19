# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.
from __future__ import annotations

import hashlib
import json
from typing import List

from secp256k1 import PrivateKey


class Event:
    def __init__(
        self,
        pubkey: str,
        created_at: int,
        kind: int,
        tags: List[List[str]],
        content: str,
        sig: str = "",
        id: str = "",
    ) -> None:
        self.pubkey = pubkey
        self.created_at = created_at
        self.kind = kind
        self.tags = tags
        self.content = content
        self.sig = sig
        self.id = id

    def calculate_id(self) -> bytes:
        event_data = [0, self.pubkey, self.created_at, self.kind, self.tags, self.content]

        serialized_event = json.dumps(event_data, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(serialized_event).digest()

    def sign_valid(self, pk: PrivateKey) -> None:
        self.sig = pk.schnorr_sign(self.calculate_id(), "").hex()

    def set_id_valid(self) -> None:
        self.id = self.calculate_id().hex()

    def to_json(self) -> str:
        event_dict = {
            "id": self.id,
            "pubkey": self.pubkey,
            "created_at": self.created_at,
            "kind": self.kind,
            "tags": self.tags,
            "content": self.content,
            "sig": self.sig,
        }
        return json.dumps(event_dict)

    def is_regular(self) -> bool:
        return self.kind < 10000 and self.kind != 0 and self.kind != 3

    def is_replaceable(self) -> bool:
        return self.kind == 0 or self.kind == 3 or (self.kind >= 10000 and self.kind < 20000)

    def is_ephemeral(self) -> bool:
        return self.kind >= 20000 and self.kind < 30000

    def is_addressable(self) -> bool:
        return self.kind >= 30000 and self.kind < 40000

    @classmethod
    def from_json(cls, json_string: str) -> Event:
        data = json.loads(json_string)
        return cls(
            data["pubkey"],
            data["created_at"],
            data["kind"],
            data["tags"],
            data["content"],
            data["sig"],
            data["id"],
        )
