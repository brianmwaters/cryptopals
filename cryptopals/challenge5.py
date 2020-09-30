"""Solution to Cryptopals Set 1, Challenge 5."""

from cryptopals.challenge2 import xor


def repeating_xor(key, bytes_):
    """Repeating-key XOR."""
    quotient = len(bytes_) // len(key)
    remainder = len(bytes_) % len(key)
    pad = key * quotient + key[:remainder]
    return xor(pad, bytes_)
