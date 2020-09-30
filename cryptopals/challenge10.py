"""Solution to Cryptopals Set 2, Challenge 10."""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptopals.challenge2 import xor
from cryptopals.challenge7 import aes_ecb_decrypt
from cryptopals.challenge8 import split_blocks


def aes_ecb_encrypt(key, pt):
    """Encrypt a byte sequence with AES-ECB."""
    encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    return encryptor.update(pt) + encryptor.finalize()


def aes_cbc_encrypt(key, iv, pt):
    """Encrypt a byte sequence with AES-CBC."""
    ct_prev = iv
    ct_blocks = []
    for pt_block in split_blocks(pt):
        ct_block = aes_ecb_encrypt(key, xor(ct_prev, pt_block))
        ct_blocks.append(ct_block)
        ct_prev = ct_block
    ct = b"".join(ct_blocks)
    return ct


def aes_cbc_decrypt(key, iv, ct):
    """Decrypt a byte sequence with AES-CBC."""
    ct_prev = iv
    pt_blocks = []
    for ct_block in split_blocks(ct):
        pt_block = xor(ct_prev, aes_ecb_decrypt(key, ct_block))
        pt_blocks.append(pt_block)
        ct_prev = ct_block
    pt = b"".join(pt_blocks)
    return pt
