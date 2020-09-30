"""Solution to Cryptopals Set 1, Challenge 7."""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def aes_ecb_decrypt(key, ct):
    """Decrypt a message encrypted with AES-ECB."""
    decryptor = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
    return decryptor.update(ct) + decryptor.finalize()
