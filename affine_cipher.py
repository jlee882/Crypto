#! /usr/bin/python3

import sys
import char_letter_mappings as conversion

# check args
if len(sys.argv) != 4:
    script_path = sys.argv[0]
    print("Usage: python3 " + script_path + " <text> <a> <b>")
    exit(1)

text = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])

def process_text(letter):
    letter_val = conversion.letter_to_num[letter]
    cipher_val = (a * letter_val + b) % 26
    return conversion.num_to_letter[cipher_val]

char_list = list(text)

for i in range(0, len(char_list)):
    char_list[i] = process_text(char_list[i])

fin_string = ''.join(char_list)
print(fin_string)
