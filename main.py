from mod import generalPurpose, passwordBase

from cryptography.fernet import Fernet
import json
import os

key = b''

filename = "pass.json"
database = []

f = None

if os.path.isfile(filename) == False:
    passwordBase.create_database(filename)
    key = Fernet.generate_key()
    f = Fernet(key)
    print(f"the key for the database, store it on a secure place: {key.decode("utf-8")}")
else:
    with open(filename, "r") as read_file:
        key = bytes(input("enter key to unlock database: "), "utf-8")
        try:
            f = Fernet(key)
        except:
            print("Invalid key")
            exit(-1)
        database = json.loads(f.decrypt(read_file.read()))
        database = generalPurpose.quicksort(database)


for entry in database:
    print("----------------------------------------------")
    print(f"user: {entry["user"]}, password: {entry["password"]}")
    print(f"Statistics:")
    print(f"lowercase: {entry["lower"]}")
    print(f"uppercase: {entry["upper"]}")
    print(f"special characters: {entry["special"]}")
    print(f"numbers: {entry["nums"]}")

unprocessed_entry = input("add entry (separated by commas ex. user, pass): ")
words = unprocessed_entry.split(",")

passwordBase.add_entry(passwordBase.create_entry(words[0], words[1]), database)
database = generalPurpose.quicksort(database)

with open(filename, "w") as write_file:
    encrypted_file = f.encrypt(bytes(json.dumps(database, indent=4), "utf-8"))
    write_file.write(encrypted_file.decode("utf-8"))
