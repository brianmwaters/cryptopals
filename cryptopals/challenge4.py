"""Solution to Cryptopals Set 1, Challenge 4."""

from cryptopals.challenge2 import xor
from cryptopals.challenge3 import is_printable, score_en


def solve(cts):
    """Solve this challenge."""
    scores = []
    cribs = [[key] * 30 for key in range(0x100)]
    for ct in cts:
        for crib in cribs:
            pt = xor(ct, crib)
            if is_printable(pt):
                scores.append((score_en(pt), pt))
    if scores:
        _, pt = max(scores)
        return pt
