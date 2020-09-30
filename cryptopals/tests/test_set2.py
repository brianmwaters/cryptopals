import binascii

from cryptopals import challenge9
from cryptopals.tests.utils import read_hex_lines, read_base64


def test_challenge9():
    input_ = b"YELLOW SUBMARINE"
    len_ = 20
    solution = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    assert challenge9.pkcs7_pad(input_, len_) == solution
    assert challenge9.pkcs7_unpad(solution, len_) == input_
