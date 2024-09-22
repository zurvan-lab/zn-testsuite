import argparse
import asyncio
import logging

import coloredlogs
from config.config import Config
from protocol.protocol import Protocol
from websockets.asyncio.client import connect


async def main() -> None:
    parser = argparse.ArgumentParser(description="znrt is nostr relay testsiute.")
    parser.add_argument("config_file", type=str, help="path to the json configuration file.")
    args = parser.parse_args()
    coloredlogs.install()

    logging.info("starting the tests...")

    cfg = Config(args.config_file)
    cfg.load()

    logging.info(f"config loaded successfully: {cfg}")

    if cfg.tests["protocol"]:
        logging.info("starting protocol tests...")

        connection1, connection2 = await connect(cfg.target), await connect(cfg.target)

        logging.info(
            f"2 connections made to relay successfully: {connection1.id} and {connection2.id}."
        )

        protocol = Protocol(cfg.get_protocol_model(), connection1, connection2)
        await protocol.run()

        await connection1.close()
        await connection2.close()


if __name__ == "__main__":
    asyncio.run(main())
