"""Solution to Cryptopals Set 1, Challenge 6."""

import bisect

from cryptopals import challenge3
from cryptopals.challenge2 import xor
from cryptopals.challenge5 import repeating_xor


# From
# https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan
def count_bits(int_):
    """Count the number of bits set in a positive integer."""
    c = 0
    while int_ != 0:
        int_ &= int_ - 1
        c = c + 1
    return c


def hamming_dist(a, b):
    """Compute the Hamming distance between two byte sequences."""
    return sum(count_bits(byte) for byte in xor(a, b))


def score_keysizes(bytes_):
    """
    Return an array of keysizes, sorted by score.

    The score is based on the Hamming distance between the first two blocks of
    the length of a given keysize.
    """
    scores = []
    for keysize in range(2, 40):
        dist = hamming_dist(bytes_[:keysize], bytes_[keysize:2*keysize])
        dist_norm = dist / keysize
        bisect.insort(scores, (dist_norm, keysize))
    return [keysize for _, keysize in scores]


def transpose(keysize, bytes_):
    """Transposes a byte sequence into blocks according to a given keysize."""
    blocks = []
    blocksize = len(bytes_) // keysize
    for i in range(keysize):
        block = bytes(bytes_[j] for j in range(i, len(bytes_), keysize))
        blocks.append(block)
    return blocks


def solve(ct):
    """Solve this challenge."""
    keysizes_scored = score_keysizes(ct)
    solutions = []
    for keysize in keysizes_scored:
        blocks = transpose(keysize, ct)
        key = bytearray(keysize)
        for i, block in enumerate(blocks):
            k = challenge3.solve(block)
            if k is not None:
                key[i] = k[0]
        key = bytes(key)
        pt = repeating_xor(key, ct)
        solutions.append((key, pt))
    # Filter out null keys
    return [(key, pt) for key, pt in solutions if any(key)]
