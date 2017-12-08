from Crypto.Cipher import AES
from base64 import b64decode

with open("7.txt") as input_file:
    cipher = b64decode(input_file.read())

x = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)
plaintext = x.decrypt(cipher)
print(plaintext)

"""
One line format:

print(AES.new("YELLOW SUBMARINE", AES.MODE_ECB).decrypt(b64decode(open("7.txt").read())))
"""
