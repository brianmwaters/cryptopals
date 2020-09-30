"""Solution to Cryptopals Set 1, Challenge 7."""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7


def aes_ecb_decrypt(key, ct):
    """Decrypt a message encrypted with AES-ECB and PKCS #7 padding."""
    decryptor = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
    unpadder = PKCS7(len(key) * 8).unpadder()
    padded = decryptor.update(ct) + decryptor.finalize()
    pt = unpadder.update(padded) + unpadder.finalize()
    return pt
