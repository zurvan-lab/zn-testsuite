from config.config import TestModel
from nostr.keys import PrivateKey
from websockets.asyncio.client import ClientConnection

from .report import Report

ALL_CASES = ["NIP-01"]


class Protocol:
    def __init__(self, cfg: TestModel, conn1: ClientConnection, conn2: ClientConnection) -> None:
        # clean up all conflicts between all cases + cases and excluded cases.
        if len(cfg.excluded_cases) != 0:
            for case in cfg.excluded_cases:
                ALL_CASES.remove(case)
                cfg.cases.remove(case)

        self.config = cfg
        self.conn1 = conn1
        self.conn2 = conn2
        self.white_listed_key1 = PrivateKey.from_hex(cfg.whitelisted_key1)
        self.white_listed_key2 = PrivateKey.from_hex(cfg.whitelisted_key2)
        self.report = Report()

    async def run(self) -> None:
        if self.config.cases.__contains__("*"):
            for case in ALL_CASES:
                await self.run_case(case)

            for case in self.config.cases:
                await self.run_case(case)

    async def run_case(self, case: str) -> None:
        if case == "NIP-01":
            await self.nip01_case()

    async def nip01_case(self) -> None:
        pass
