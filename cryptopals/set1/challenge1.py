"""Solution to Cryptopals Set 1, Challenge 1."""

from binascii import a2b_hex, b2a_base64


def hex2base64(hexstr):
    """Convert a hex string to a base64 string."""
    return b2a_base64(a2b_hex(hexstr), newline=False)
