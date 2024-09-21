import argparse
import asyncio

from config.config import Config
from protocol.protocol import Protocol
from websockets.asyncio.client import connect


async def main() -> None:
    parser = argparse.ArgumentParser(description="znrt is nostr relay testsiute.")
    parser.add_argument("config_file", type=str, help="path to the json configuration file.")
    args = parser.parse_args()

    cfg = Config(args.config_file)
    try:
        cfg.load()
        print("configuration loaded successfully:")
        print(cfg)
    except Exception as e:
        print(f"failed to load configuration: {e}")

    if cfg.tests["protocol"]:
        connection1, connection2 = await connect(cfg.target), await connect(cfg.target)
        protocol = Protocol(cfg.get_protocol_model(), connection1, connection2)
        protocol.run()
        await connection1.close()
        await connection2.close()


if __name__ == "__main__":
    asyncio.run(main())
