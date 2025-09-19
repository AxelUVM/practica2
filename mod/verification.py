# verificacion de contraseñas
# crea una tupla con los conteos y la regresa

def verify(pswd: str) -> tuple:
    lower = __count_lower(pswd)
    upper = __count_upper(pswd)
    special = __count_special(pswd)
    nums = __count_numeric(pswd)

    return (lower, upper, special, nums)


# funcion privada para contar las mayusculas
def __count_upper(pswd: str) -> int:
    count = 0
    for char in pswd:
        if char.isupper():
            count += 1
    return count


# funcion privada para contar las minusculas
def __count_lower(pswd: str) -> int:
    count = 0
    for char in pswd:
        if char.islower():
            count += 1
    return count

# funcion privada para contar los caracteres especiales
def __count_special(pswd: str) -> int:
    count = 0
    for char in pswd:
        if not (char.isalpha() or char.isdigit() or char == ' '):
            count += 1
    return count

# funcion privada para contar los numeros
def __count_numeric(pswd: str) -> int:
    count = 0
    for char in pswd:
        if char.isdigit():
            count +=1
    return count
