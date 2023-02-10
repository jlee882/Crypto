#! /usr/bin/python3

import sys
import char_letter_mappings as conversion

# check args
if len(sys.argv) != 4:
    script_path = sys.argv[0]
    print("Usage: python3 " + script_path + " <enc/dec> <text file> <key>")
    exit(1)

action = sys.argv[1]
key = sys.argv[3]
key_len = len(key)

f = open(sys.argv[2], "r")
text = f.read()
text = text.strip()
text = text.replace(" ", "")
text = text.replace("\n", "")
text = text.upper()

shift_direction = 1 if action == "enc" else -1

# encoding/decoding
def key_char(position, key, key_length):
    index = position % key_length
    return key[index]


char_list = list(text)

for i in range(0, len(char_list)):
    letter = char_list[i]
    shift_char = key_char(i, key, key_len)
    shift = shift_direction * conversion.letter_to_num[shift_char]
    new_num = (conversion.letter_to_num[letter] + shift) % 26
    char_list[i] = conversion.num_to_letter[new_num]

fin_string = ''.join(char_list)
print(fin_string)