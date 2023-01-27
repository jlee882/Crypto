#! /bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <enc/dec> <text>"
    exit 1
fi

action=$1
text=$2

script="./shift_cipher.py"
direction=0
if [ $action == "dec" ]; then
    direction=-1
elif [ $action == "enc" ]; then
    direction=1
else
    echo "No encrypt or decrypt action specified"
    exit 1
fi

for i in {0..25}; do
    echo -n "Shift by $i: "
    python3 ./shift_cipher.py $action $text $i
done
