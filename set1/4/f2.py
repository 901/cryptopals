import sys
from word_score import word_score

fo = open("4.txt", "r")
fitness = word_score()
decrypted = b''
decrypted_strings = []
fitness_dict = {}

def pretty_print_result(result):
    """Prints the given resulting candidate in a pretty format."""
    print(result['plaintext'].decode().rstrip(), "\tScore:", "{0:.2f}".format(result['score']),
          "\tKey:", chr(result['key']))

for ctext in fo:
    #ctext = fo.readline()
    #print ctext
    ctext = bytes.fromhex(ctext)
    for a in range(0,256):
        for c in ctext:
            decrypted += bytes([a ^ c])
        pretty_print_result(decrypted)

for i in range(0, len(decrypted_strings)):
    x, y = fitness.score(decrypted_strings[i])
    #print i
    if x > -51.0:
        print(" " + str(x) + "  " + decrypted_strings[i])
    fitness_dict[decrypted_strings[i]] = x

highest = max(fitness_dict.values())

for k,v in fitness_dict.iteritems():
    if v == highest:
        print(k)
