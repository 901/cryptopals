from base64 import b64decode
from itertools import combinations

def hamming_distance(binary_seq_1, binary_seq_2):
    """Computes the edit distance/Hamming distance between two equal-length strings."""
    assert len(binary_seq_1) == len(binary_seq_2)
    dist = 0

    for bit1, bit2 in zip(binary_seq_1, binary_seq_2):
        diff = bit1 ^ bit2
        dist += sum([1 for bit in bin(diff) if bit == '1'])

    return dist

print(hamming_distance(b"wokka wokka!!!", b"this is a test"))
