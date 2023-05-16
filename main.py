""" Números compremetidos """
# Cómo hacer un programa para buscar números comprometidos en Python.
''' Se define como par de números compretidos, al par de números tal que, la suma de divisores (excepto el 1 y el mimo número) es igual al otro y viceversa. Por Ejemplo el 48 y el 75. Los divisores de 48 son 2, 3, 4, 6, 8, 12, 16, 24, que sumados nos da 75. Aśi mismo los divisores de 75 son 3, 5, 15, 25, que sumados nos da 48. '''

# Primeramente calculamos la suma de divisores de un número.
def Suma_divisores(x):
    suma = 0
    y = 2
    while y <= x // 2:
        if x % y == 0:
            suma += y
        y += 1
    return suma

# Buscamos la parejea de un número.
def Buscar_pareja(x):
    posible_pareja = Suma_divisores(x)
    if Suma_divisores(posible_pareja) == x:
        return posible_pareja
    else:
        return -1

# Por ultimo haremos una función que nos permita elegir cuantas parejas de números comprometidos queremos encontrar.
def Buscar_números_comprometidos(x):
    numero_de_parejas = 0
    ultimo_encotrado = 0

    while numero_de_parejas < x:
        posible_pareja = Buscar_pareja(ultimo_encotrado + 1)
        if posible_pareja != -1 and ultimo_encotrado + 1 < posible_pareja:
            numero_de_parejas += 1
            print(ultimo_encotrado + 1, posible_pareja)
        ultimo_encotrado += 1

# Listo, ya tenemos un buscador de parejas de números compromeridos.
# Ahora escribiremos unas pequeñas lineas de código para poder interactuar con nuestro programa a traves de la terminal.
print("Buscador de parejas de números comprometidos")
número_de_parejas_a_buscar = input("Ingresa el número de parejas: ")
if número_de_parejas_a_buscar.isdigit():
    Buscar_números_comprometidos(int(número_de_parejas_a_buscar))
else:
    print("Opción no valida")