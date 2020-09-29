"""Solution to Cryptopals Set 2, Challenge 9."""

from cryptography.hazmat.primitives.padding import PKCS7


def pad(bytes_, length):
    """Implement PKCS #7 padding."""
    padder = PKCS7(length * 8).padder()
    return padder.update(bytes_) + padder.finalize()
