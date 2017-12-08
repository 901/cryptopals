import sys
from word_score import word_score

#test 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def get_english_score(input_bytes):
    """Returns a score which is the sum of the probabilities in how each letter of the input data
    appears in the English language. Uses the above probabilities.
    """
    score = 0

    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)

    return score

#decryption key is a single character in the alphabet
decrypted = b""
cipher = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

decrypted_strings = []
fitness_dict = {} #dictionary to assign (string, fitness) key, value to decide on best possible decrypted message

#test each possible letter of the alphabet as the key
for c1 in range(0, 256):
    for c2 in cipher:
        decrypted += bytes(c1 ^ c2)
    decrypted_strings.append(decrypted) #add potential ciphertext to the list of decrypted strings
    decrypted = ""


for i in range(0, len(decrypted_strings)):
    #we only need the score, so add the score to the fitness dictionay, with the string as key
    fitness_dict[decrypted_strings[i]] = get_english_score(decrypted_strings[i])

#find the highest fitness score in the dictionary
highest_score = max(fitness_dict.values())
print(highest_score)
#iterate through all of the dictionary and find maching string given highest score value
for k,v in fitness_dict.iteritems():
    if v == highest_score:
        print(k)
