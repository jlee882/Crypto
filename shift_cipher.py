#! /usr/bin/python3

import sys
import char_letter_mappings as conversion

# check args
if len(sys.argv) != 4:
    script_path = sys.argv[0]
    print("Usage: python3 " + script_path + " <enc/dec> <text> <shift>")
    exit(1)

action = sys.argv[1]
text = sys.argv[2]
shift = int(sys.argv[3])


if action == "dec":
    # shift opposite direction
    shift = shift * (-1)

# encoding/decoding
char_list = list(text)

for i in range(0, len(char_list)):
    letter = char_list[i]
    new_num = (conversion.letter_to_num[letter] + shift) % 26
    char_list[i] = conversion.num_to_letter[new_num]

fin_string = ''.join(char_list)
print(fin_string)
