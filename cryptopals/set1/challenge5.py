"""Solution to Cryptopals Set 1, Challenge 5."""

from cryptopals.set1 import challenge2


def xor(key, message):
    """Repeating-key XOR."""
    quotient = len(message) // len(key)
    remainder = len(message) % len(key)
    pad = key * quotient + key[:remainder]
    return challenge2.xor(pad, message)
