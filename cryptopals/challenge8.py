"""Solution to Cryptopals Set 1, Challenge 8."""

import math


def split_blocks(bytes_):
    """Split a byte sequence into 16-byte blocks."""
    return [bytes_[start:start+16] for start in range(0, len(bytes_), 16)]


def score_ecb(bytes_):
    """
    Score a byte sequence based on likliehood it is an ECB mode ct.

    The score is based on the standard deviation of the distribution of 16-byte
    blocks in the sequence.
    """
    blocks = split_blocks(bytes_)
    repeats = {}
    for block in blocks:
        if block not in repeats.keys():
            repeats[block] = 1
        else:
            repeats[block] += 1
    distribution = repeats.values()
    sigma = math.sqrt(sum(x ** 2 for x in distribution)) / len(blocks)
    return sigma


def solve(cts):
    """Solve this challenge."""
    scores = []
    for ct in cts:
        scores.append((score_ecb(ct), ct))
    if scores:
        _, ct = max(scores)
        return ct
