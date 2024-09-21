import json
from typing import List


class Report:
    def __init__(self) -> None:
        self.supportes_nips: List[int] = []
        self.errors: List[str] = []

    def add_nip(self, nip: int):
        self.supportes_nips.append(nip)

    def add_error(self, error: str):
        self.errors.append(error)

    def to_json(self) -> str:
        event_dict = {"nips": self.supportes_nips, "errors": self.errors}
        return json.dumps(event_dict)
