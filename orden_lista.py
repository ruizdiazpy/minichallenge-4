numeros = input("Introduce una lista de números separados por espacios: ")

lista_numeros = list(map(int, numeros.split()))

lista_numeros.sort()

print("Lista ordenada en orden ascendente:", lista_numeros)
