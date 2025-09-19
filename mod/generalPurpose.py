# Algoritmo para ordenar las contraseña.
# quicksort funciona de la siguiente manera
# con una lista `arr`, 
# si la longitud de `arr` es menor o igual a 1 regresa la lista como ésta ya que esta ya ésta ordenada
# se crea un pivote, puede ser el primer elemento, el ultimo elemento o el de en medio de la lista. (en este caso el primero)
# se divide la lista en 2 partes (lo o left y hi o right)
# si el elemento actual es menor al pivote se agrega a lo o si el elemento actial es mayor o igual al pivote se agrega a hi
# se llama recursivamente quicksort en las listas lo y hi
# concatena la lista lo ordenada, el pivote y la lista hi ordenada
# se regresa la lista concatenada
# complejidad de tiempo O(n log n)

def quicksort(arr: list[dict]) -> list[dict]:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]["password"]
        lo = [x for x in arr[1:] if len(x["password"]) < len(pivot)]
        hi = [x for x in arr[1:] if len(x["password"]) >= len(pivot)]
        return quicksort(lo) + [arr[0]] + quicksort(hi)
