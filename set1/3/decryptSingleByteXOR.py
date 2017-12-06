import sys
from word_score import word_score

#test 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

#decryption key is a single character in the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
decrypted = ""
cipher = sys.argv[1].decode("hex")

decrypted_strings = []
fitness_dict = {} #dictionary to assign (string, fitness) key, value to decide on best possible decrypted message
fitness = word_score() #word_score assigns a word likelihood score to some given decrypted ciphertext

#test each possible letter of the alphabet as the key
for c1 in alphabet:
    for c2 in cipher:
        decrypted += chr((ord(c1) ^ ord(c2)))
    decrypted_strings.append(decrypted) #add potential ciphertext to the list of decrypted strings
    decrypted = ""


for i in range(0, len(decrypted_strings)):
    #returns (score, list object of possible substrings in ciphertext) tuple
    x, y = fitness.score(decrypted_strings[i])
    #print str(x) + " " + decrypted_strings[i]
    #we only need the score, so add the score to the fitness dictionay, with the string as key
    fitness_dict[decrypted_strings[i]] = x

#find the highest fitness score in the dictionary
highest_score = max(fitness_dict.values())
print highest_score
#iterate through all of the dictionary and find maching string given highest score value
for k,v in fitness_dict.iteritems():
    if v == highest_score:
        print k
