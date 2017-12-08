from base64 import b64decode
from itertools import combinations

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

""" Naive word-fitness function:
    Returns sum of character frequency scores to analyze word fitness"""
def get_english_score(input_bytes):
    score = 0
    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)

    return score

"""Computes Hamming distance between two equal-length strings."""
def hamming_distance(bstring1, bstring2):
    assert len(bstring1) == len(bstring2) #strings must be equal length in operation
    dist = 0

    for b1, b2 in zip(bstring1, bstring2):
        diff = b1 ^ b2
        dist += sum([1 for bit in bin(diff) if bit == '1'])
    return dist

"""XORs every byte of the input with the given key character (key_value) and returns the result."""
def singlechar_xor(input_bytes, key_value):
    output = b''
    for char in input_bytes:
        output += bytes([char ^ key_value])
    return output

"""Tries every possible byte for the single-char key, decrypts the ciphertext with that byte
and computes the english score for each plaintext. The plaintext with the highest score
is likely to be the one decrypted with the correct value of key.
"""
def singlechar_xor_brute_force(ciphertext):
    candidates = []
    for key_candidate in range(256):
        plaintext_candidate = singlechar_xor(ciphertext, key_candidate)
        candidate_score = get_english_score(plaintext_candidate)

        #create a result dictionary to store each candidate plaintext
        result = {
            'key': key_candidate,
            'score': candidate_score,
            'plaintext': plaintext_candidate
        }

        candidates.append(result)

    # Return the candidate with the highest English score
    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]

"""Encrypts plaintext with repeating Key (key) with XOR"""
def repeating_key_xor(plaintext, key):
    ciphertext = b''
    i = 0

    for byte in plaintext:
        ciphertext += bytes([byte ^ key[i]])
        i += 1
        i = i % 3 #cycle i position
    return ciphertext

def break_repeating_key_XOR(data):
    normalized_distances = {} #will hold the normalized hamming distances of possible strings

    #A proposed option in the challenge was to break the text into first 4 chunks of length key_size
    for key_size in range(2,41):
        chunks = [data[i:i + key_size] for i in range(0, len(data), key_size)][:4]

        distance = 0
        pairs = combinations(chunks, 2) #take pairs of strings, and sum their hamming distances
        for a,b in pairs:
            distance += hamming_distance(a,b)

        avg_distance = distance / 6
        normalized_dist = avg_distance / key_size
        normalized_distances[key_size] = normalized_dist

    #want the key_sizes that yield the best normalized distance
    possible_key_sizes = sorted(normalized_distances, key=normalized_distances.get)[:3]
    possible_messages = []

    for x in possible_key_sizes:
        key = b''

        #break up ciphertext into blocks of key_size length
        for i in range(x):
            block = b''

            #Transpose step (suggested option): make a block that is the i-th byte of every block
            for j in range(i, len(data), x):
                block += bytes(data[j])

            #we can perform single character XOR brute force on the blocks
            key += bytes([singlechar_xor_brute_force(block)['key'])

        possible_messages.append((repeating_key_xor_(data, key), key))
    #want to return the best possible messages (ranked by their word-fitness)
    return max(possible_messages, key=lambda k: get_english_score(k[0]))

with open("6.txt") as input_file:
    data = b64decode(input_file.read())

result = break_repeating_key_XOR(data)
print("Key = " + result[1].decode())
print("---------------------------------------")
print(result[0].decode().rstrip())
