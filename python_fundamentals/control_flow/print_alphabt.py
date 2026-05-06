#!/usr/bin/env python3

result = ""

for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != "q" and letter != "e":
        result += letter

print("{}".format(result), end="")
