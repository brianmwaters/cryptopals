"""Solution to Cryptopals Set 1, Challenge 4."""

from cryptopals.set1 import challenge2, challenge3


def solve(ciphertexts):
    """Solve this challenge."""
    scores = []
    cribs = [[key] * 30 for key in range(0x100)]
    for ciphertext in ciphertexts:
        for crib in cribs:
            plaintext = challenge2.xor(ciphertext, crib)
            if challenge3.isprintable(plaintext):
                scores.append((challenge3.score_en(plaintext), plaintext))
    if scores:
        _, plaintext = max(scores)
        return plaintext
