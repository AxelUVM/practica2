from mod import generalPurpose, passwordBase
import json
import os

filename = "pass.json"
database = []

if os.path.isfile(filename) == False:
    passwordBase.create_database(filename)
else:
    with open(filename, "r") as read_file:
        database = json.load(read_file)   
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
    json.dump(database, write_file, indent=4)
