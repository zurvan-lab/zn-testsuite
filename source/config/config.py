from __future__ import annotations

import json
from typing import Dict, List, Union

# refactor this package!!!!!!!!!!!!


class Config:
    def __init__(self, path: str) -> None:
        self.path = path
        self.name: str = ""
        self.target: str = ""
        self.tests: Dict[str, Dict[str, str | List[str]]] = {}

    def load(self) -> None:
        with open(self.path) as f:
            jr = json.load(f)
            self.name = jr["name"]
            self.target = jr["target"]
            self.tests = jr["tests"]

    def to_dict(self) -> Dict[str, Union[str, Dict[str, Dict[str, str | List[str]]]]]:
        return {"name": self.name, "target": self.target, "tests": self.tests}

    def get_protocol_model(self) -> TestModel:
        p = self.tests["protocol"]
        return TestModel(
            str(p["outdir"]),
            list(p["cases"]),
            list(p["excluded_cases"]),
            str(p["whitelisted_key1"]),
            str(p["whitelisted_key2"]),
        )

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


class TestModel:
    def __init__(
        self, outdir: str, cases: List[str], excluded_cases: List[str], key1: str, key2: str
    ) -> None:
        self.outdir = outdir
        self.cases = cases
        self.excluded_cases = excluded_cases
        self.whitelisted_key1 = key1
        self.whitelisted_key2 = key2

    def to_dict(self) -> Dict[str, Union[str, List[str]]]:
        return {
            "outdir": self.outdir,
            "cases": self.cases,
            "excluded_cases": self.excluded_cases,
            "whitelisted_key2": self.whitelisted_key2,
            "whitelisted_key1": self.whitelisted_key1,
        }
