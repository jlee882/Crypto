#! /usr/bin/python3
import sys

if len(sys.argv) != 3:
    script_path = sys.argv[0]
    print("Usage: python3 " + script_path + " <ciphertext file path> <num groups>")
    exit(1)

file = sys.argv[1]
num_groups = int(sys.argv[2])

f = open(file, "r")

ciphertext = f.read()
ciphertext = ciphertext.replace(" ", "")
ciphertext = ciphertext.replace("\n", "")
ciphertext = ciphertext.upper()

ciphertext_len = len(ciphertext)

group_list = []
for i in range(0, num_groups):
    group_list.append("")

# separate ciphertext into the groups
for i in range(0, ciphertext_len):
    group = i % num_groups
    group_list[group] += ciphertext[i]

# print all groups
for i in range(0, num_groups):
    print("Group " + str(i + 1))
    print(group_list[i])

