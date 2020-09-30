"""Solution to Cryptopals Set 2, Challenge 9."""

from cryptography.hazmat.primitives.padding import PKCS7


def pkcs7_pad(bytes_, len_):
    """Implement PKCS #7 padding."""
    padder = PKCS7(len_ * 8).padder()
    return padder.update(bytes_) + padder.finalize()
