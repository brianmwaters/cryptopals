import binascii

from cryptopals.set2 import challenge9
from cryptopals.tests.utils import read_hex_lines, read_base64


def test_challenge9():
    input_ = b"YELLOW SUBMARINE"
    length = 20
    solution = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    assert challenge1.pad(input_, length) == solution
