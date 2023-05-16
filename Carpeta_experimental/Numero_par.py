""" Pequeño programa que nos avisa si un numero es par o impar """

def Es_par(num):
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    while True:
        a = input("Ingrese un numero entero")
        if a.isdigit():
            a = int(a)
            break
    if Es_par(a):
        print(f"El número {a} es par")
    else:
        print(f"El número {a} es impar")