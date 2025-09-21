from mod import generalPurpose, passwordBase

from cryptography.fernet import Fernet
import json
import os

key = None
f = None

database = []

filename = input("Plase enter the name of your database: ") + ".json"

if os.path.isfile(filename) == False:
    passwordBase.create_database(filename)
    key = Fernet.generate_key()
    f = Fernet(key)
    print(f"the key for {filename}, store it on a secure place: {key.decode("utf-8")}")
else:
    with open(filename, "r") as read_file:
        key = bytes(input("enter key to unlock database: "), "utf-8")
        try:
            f = Fernet(key)
        except:
            raise ValueError("Invalid Key")
            exit(-1)
        database = json.loads(f.decrypt(read_file.read()))
        database = generalPurpose.quicksort(database)

while(True):
    print("Welcome to the <Axel Flores Teja> Password Manager")
    print(f"1. Add entry to database '{filename}'")
    print(f"2. Check statistics of every password in {filename}")
    print(f"3. Exit")

    try:
        option = int(input("> "))
    except ValueError:
        raise ValueError("Option MUST be an integer")
    
    match option:
        case 1:
            generalPurpose.clear()
            unprocessed_entry = input("add entry (separated by commas ex. user, pass): ")
            words = unprocessed_entry.split(",")

            passwordBase.add_entry(passwordBase.create_entry(words[0], words[1]), database)
            database = generalPurpose.quicksort(database)
            input("Press any key to continue...")
            generalPurpose.clear()
        case 2:
            generalPurpose.clear()
            for entry in database:
                print("----------------------------------------------")
                print(f"user: {entry["user"]}, password: {entry["password"]}")
                print(f"Statistics:")
                print(f"lowercase: {entry["lower"]}")
                print(f"uppercase: {entry["upper"]}")
                print(f"special characters: {entry["special"]}")
                print(f"numbers: {entry["nums"]}")
            input("Press any key to continue...")
            generalPurpose.clear()
        case 3:
            print("saving changes")
            print("encrypting file...")
            print("Byeeeee :3")

            with open(filename, "w") as write_file:
                encrypted_file = f.encrypt(bytes(json.dumps(database, indent=4), "utf-8"))
                write_file.write(encrypted_file.decode("utf-8"))
            exit(0)
        case 4:
            generalPurpose.clear()
            print(f"{option} not an option")
            input("Press any key to continue...")
            generalPurpose.clear()
