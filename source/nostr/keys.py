from __future__ import annotations

import os
import secrets

import secp256k1


class PublicKey:
    def __init__(self, raw_bytes: bytes = b"") -> None:
        self.raw_bytes = raw_bytes

    def hex(self) -> str:
        return self.raw_bytes.hex()

    def verify_signed_message_hash(self, hash: str, sig: str) -> bool:
        pk = secp256k1.PublicKey(b"\x02" + self.raw_bytes, True)
        return pk.schnorr_verify(bytes.fromhex(hash), bytes.fromhex(sig), None, True)


class PrivateKey:
    def __init__(self, raw_secret: bytes = b"") -> None:
        if raw_secret is not None:
            self.raw_secret = raw_secret
        else:
            self.raw_secret = secrets.token_bytes(32)

        sk = secp256k1.PrivateKey(self.raw_secret)
        self.public_key = PublicKey(sk.pubkey.serialize()[1:])

    @classmethod
    def from_hex(cls, hex: str) -> PrivateKey:
        return cls(bytes.fromhex(hex))

    def hex(self) -> str:
        return self.raw_secret.hex()

    def sign_message_hash(self, hash: bytes) -> str:
        sk = secp256k1.PrivateKey(self.raw_secret)
        sig = sk.schnorr_sign(hash, None, raw=True)
        return sig.hex()

    @classmethod
    def get_random_key(cls) -> PrivateKey:
        return cls(os.urandom(32))

    def __eq__(self, other):
        return self.raw_secret == other.raw_secret
