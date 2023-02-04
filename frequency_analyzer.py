#! /usr/bin/python3
import sys
import english_letter_frequency as eng_freq

def freq_sorter(dictionary):
    sorted_output = sorted(dictionary.items(), key = lambda x: x[1], reverse = True)
    return sorted_output

if len(sys.argv) != 2:
    script_path = sys.argv[0]
    print("Usage: python3 " + script_path + " <ciphertext file path>")
    exit(1)

file = sys.argv[1]

f = open(file, "r")

ciphertext = f.read()
ciphertext = ciphertext.strip()
ciphertext = ciphertext.upper()

ciphertext_len = len(ciphertext)

ciphertext_freq = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    "D" : 0,
    "E" : 0,
    "F" : 0,
    "G" : 0,
    "H" : 0,
    "I" : 0,
    "J" : 0,
    "K" : 0,
    "L" : 0,
    "M" : 0,
    "N" : 0,
    "O" : 0,
    "P" : 0,
    "Q" : 0,
    "R" : 0,
    "S" : 0,
    "T" : 0,
    "U" : 0,
    "V" : 0,
    "W" : 0,
    "X" : 0,
    "Y" : 0,
    "Z" : 0
}

for i in ciphertext:
    ciphertext_freq[i] += 1;

for key in ciphertext_freq:
    ciphertext_freq[key] = round(ciphertext_freq[key] / ciphertext_len, 3)

ciphertext_freq = freq_sorter(ciphertext_freq)
sorted_eng_freq = freq_sorter(eng_freq.frequency)

for i in range(0, 26):
    print(str(ciphertext_freq[i]) + "\t" + str(sorted_eng_freq[i]))

