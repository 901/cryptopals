from binascii import hexlify


def repeating_key_XOR(plaintext, key):
    ciphertext = b""
    position = 0

    for byte in plaintext
        #ciphertext += [byte ^ key[position]]
        print("XORing " + byte + " with " + key[position])
        position += 1
        position = (position % 3)

    return ciphertext

c = repeating_key_XOR(b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", b'ICE')
print("\n")
print(str(hexlify(c), "utf-8"))
