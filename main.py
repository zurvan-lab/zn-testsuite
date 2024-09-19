
from secp256k1 import PrivateKey

from nostr.event import Event
from nostr.message import Message


def main() -> None:
    pk = PrivateKey()
    evt  = Event(pk.serialize(), 123566, 1, [["e", "werfg"]], "efefFEFFEWEF")
    evt.set_id_valid()
    evt.sign_valid(pk)

    msg = Message("EVENT", evt.to_json())
    print(msg.to_json())


main()
