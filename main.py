from secp256k1 import PrivateKey

from nostr.event import Event
from nostr.filter import Filter
from nostr.message import Message


def main() -> None:
    pk = PrivateKey()
    evt = Event(
        pk.serialize(),
        123566,
        1,
        [["1111", "sss"], ["e", "some_event_id"], ["e", "another_id"], ["e"]],
        "efefFEFFEWEF",
    )
    evt.set_id_valid()
    evt.sign_valid(pk)

    msg = Message("EVENT", evt)
    print(msg.to_json())
    print(evt.is_ephemeral())  # False
    print(evt.is_regular())  # True

    f = Filter(ids=[evt.calculate_id().hex()])
    print(f.match(evt))  # True

    f = Filter(tag_filters={"#e": ["some_event_id"]})
    print(f.match(evt))  # True


main()
