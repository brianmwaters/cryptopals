"""Solution to Cryptopals Set 1, Challenge 2."""


def xor(a, b):
    """XOR two byte sequences together."""
    return bytes(za ^ zb for za, zb in zip(a, b))
