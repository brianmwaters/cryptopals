"""Solution to Cryptopals Set 1, Challenge 7."""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7


def decrypt(key, ciphertext):
    """Decrypt a message encrypted with AES-ECB and PKCS #7 padding."""
    decryptor = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
    unpadder = PKCS7(len(key) * 8).unpadder()
    padded = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = unpadder.update(padded) + unpadder.finalize()
    return plaintext
