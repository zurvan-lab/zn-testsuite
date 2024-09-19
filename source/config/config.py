from __future__ import annotations

import json
from typing import Dict, List, Union


class Config:
    def __init__(self, path: str) -> None:
        self.path = path
        self.name: str = ""
        self.target: str = ""
        self.tests: Dict[str, ProtocolModel] = {}

    def load(self) -> None:
        with open(self.path) as f:
            jr = json.load(f)
            self.name = jr["name"]
            self.target = jr["target"]
            self.tests = jr["tests"]

    def to_dict(self) -> Dict[str, Union[str, Dict[str, ProtocolModel]]]:
        return {"name": self.name, "target": self.target, "tests": self.tests}

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


class ProtocolModel:
    def __init__(self, outdir: str, cases: List[str], excluded_cases: List[str]) -> None:
        self.outdir = outdir
        self.cases = cases
        self.excluded_cases = excluded_cases

    def to_dict(self) -> Dict[str, Union[str, List[str]]]:
        return {"outdir": self.outdir, "cases": self.cases, "excluded_cases": self.excluded_cases}
