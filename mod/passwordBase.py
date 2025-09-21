from mod import verification

# crea un diccionario con el usuario, la contraseña, y las estadisticas verificadas
def create_entry(user: str, pswd: str) -> dict:
    lower, upper, special, nums = verification.verify(pswd)

    return {"user": user, "password": pswd, "lower": lower, "upper": upper, "special": special, "nums": nums}

# agrega una entrada a la lista de contraseñas
def add_entry(entry: dict, pswd_list: list):
   pswd_list.append(entry) 

# crea la lista de contraseñas
def create_database(filename: str):
    print("Creating password file...")
    open(filename, "w")
