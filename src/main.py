import asyncio

from nostr_sdk import Client, EventBuilder, Keys, NostrSigner


async def main() -> None:
    keys = Keys.generate()
    client = Client(NostrSigner.keys(keys))

    await client.add_relays(["wss://relay"])
    await client.connect()

    event = EventBuilder.text_note("hello from znt.", [])
    _ = await client.send_event_builder(event)

asyncio.run(main())
