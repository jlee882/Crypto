#! /usr/bin/python3
import sys

if len(sys.argv) != 2:
    script_path = sys.argv[0]
    print("Usage: python3 " + script_path + " <ciphertext file path>")
    exit(1)

file = sys.argv[1]

f = open(file, "r")

ciphertext = f.read()
ciphertext = ciphertext.replace(" ", "")
ciphertext = ciphertext.replace("\n", "")
ciphertext = ciphertext.upper()

ciphertext_len = len(ciphertext)

for shift in range(ciphertext_len):
    matches = 0
    for i in range(ciphertext_len):
        j = (i + shift) % ciphertext_len

        if ciphertext[i] == ciphertext[j]:
            matches += 1
    
    print("Matches with shift " + str(shift) + ": " + str(matches))