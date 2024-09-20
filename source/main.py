import argparse
import asyncio
import binascii
import os

from config.config import Config
from nostr.event import Event
from nostr.message import Message
from nostr.keys import PrivateKey, PublicKey
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
        async with connect(cfg.target) as connection:
            private_key_bytes = os.urandom(32)
            sec = PrivateKey(private_key_bytes)
            pub = sec.public_key.hex()
            event = Event(pub, 1726846204, 1, [], "test")
            event.sign_valid(sec)
            event.set_id_valid()
            print(event.to_json())
            msg = Message("EVENT", event)
            await connection.send(msg.to_json())

            resp = await connection.recv()
            print(resp)


if __name__ == "__main__":
    asyncio.run(main())
