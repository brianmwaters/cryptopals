"""Utility functions for test suite."""

import binascii
import os

test_root = os.path.dirname(__file__)


def read_hex_lines(path):
    """Read a file of hex lines."""
    file_ = open(os.path.join(test_root, path))
    return [binascii.a2b_hex(line.strip()) for line in file_.readlines()]


def read_base64(path):
    """Read a base64-encoded file."""
    file_ = open(os.path.join(test_root, path))
    return binascii.a2b_base64(file_.read())
