"""Solution to Cryptopals Set 1, Challenge 3."""

import math
import string

from cryptopals.set1 import challenge2

# English letter frequencies distribution from A to Z. From
# http://norvig.com/mayzner.html.
ENGLISH_FREQ = [
    0.0804,
    0.0148,
    0.0334,
    0.0382,
    0.1249,
    0.0240,
    0.0187,
    0.0505,
    0.0757,
    0.0016,
    0.0054,
    0.0407,
    0.0251,
    0.0723,
    0.0764,
    0.0214,
    0.0012,
    0.0628,
    0.0651,
    0.0928,
    0.0273,
    0.0105,
    0.0168,
    0.0023,
    0.0166,
    0.0009,
]


def letterize(bytes_):
    """
    Canonicalize a byte sequence.

    Removes non-alphabetic characters and converts to lower case.
    """
    return bytes(b for b in bytes_ if chr(b).isalpha()).lower()


def frequencies(bytes_):
    """Compute the letter frequency distribution of a byte sequnce."""
    letters = letterize(bytes_)
    counts = [0 for _ in range(26)]
    for letter in letters:
        counts[letter - ord("a")] += 1
    if len(letters) > 0:
        freqs = [count / len(letters) for count in counts]
    else:
        freqs = counts  # all zero's
    return freqs


def euclid_dist(a, b):
    """Compute the Euclidian  distance between two sequences."""
    return math.sqrt(sum((za - zb) ** 2 for za, zb in zip(a, b)))


def score_en(bytes_):
    """
    Compute an English language score for a byte sequence.

    The score is based on the similarity of the distribution of letters in the
    byte sequence to that of English, and the percentage of bytes which are
    alphabetic ASCII characters.
    """
    # Score based on similarity of letter frequencies to English
    freq_score = 1 - euclid_dist(frequencies(bytes_), ENGLISH_FREQ)
    # Score based on % of alphabetic characters
    alpha_score = sum(1 for b in bytes_ if chr(b).isalpha()) / len(bytes_)
    return freq_score * alpha_score


def isprintable(bytes_):
    """Test whether a byte sequence is a printable ASCII string."""
    return all(chr(b) in string.printable for b in bytes_)


def solve(ciphertext):
    """
    Solve this challenge.

    Trying all possible keys, this throws out plaintext candidates that aren't
    printable ASCII strings, and and returns the candidate with the highest
    score.
    """
    scores = []
    for key in range(0x100):
        crib = [key] * len(ciphertext)
        plaintext = challenge2.xor(ciphertext, crib)
        if isprintable(plaintext):
            scores.append((score_en(plaintext), key, plaintext))
    if scores:
        _, key, plaintext = max(scores)
        return key, plaintext
