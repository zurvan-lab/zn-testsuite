# this nostr module is designed to give a good ability of manipulating to higher layer.
# then we can perform flexible tests using it and expect failures.
# this library it not aimed to be used on relay/client codes.

import hashlib
import json

from secp256k1 import PrivateKey

# TODO::: invalid event, random event, check equity, kind range and more.

class Event:
    def __init__(self, pubkey: str, created_at: int, kind: int, tags, content: str):
        self.pubkey = pubkey
        self.created_at = created_at
        self.kind = kind
        self.tags = tags
        self.content = content
        self.sig = None

    def calculate_id(self):
        event_data = [
            0,
            self.pubkey,
            self.created_at,
            self.kind,
            self.tags,
            self.content
        ]

        serialized_event = json.dumps(event_data, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(serialized_event).digest()

    def sign_valid(self, pk: PrivateKey):
       self.sig = pk.schnorr_sign(self.calculate_id(), "").hex()

    def set_id_valid(self):
       self.id = self.calculate_id().hex()

    def to_json(self):
        event_dict = {
            "id": self.id,
            "pubkey": self.pubkey,
            "created_at": self.created_at,
            "kind": self.kind,
            "tags": self.tags,
            "content": self.content,
            "sig": self.sig
        }
        return json.dumps(event_dict)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        event = cls(data["pubkey"], data["created_at"], data["kind"], data["tags"], data["content"], data.get("sig"))
        return event
