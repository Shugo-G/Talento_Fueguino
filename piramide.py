base = int(input(f"Ingre un numero entero positivo para base de la pirámide: "))

def piramide(base):
    print("Pirámide :")
    for i in range (1, base + 1):
        print("*" * i)

def piramide_invertida(base):
    print("Pirámide Invertida: ")
    for i in range (0, base):
        print("*" * (base - i))

def piramide_egipcia(base):
    print("Pirámide Egipcia: ")
    i = 0
    while (2 * i + 1) <= base:
        espacios = " " * (base - (i))
        ladrillos = "*" * (2 * i + 1)
        print(espacios + ladrillos)
        i += 1

def piramide_egipcia_inv(base):
    print("Pirámide Egipcia Invertida: ")
    i = 0
    while base > 0:
        espacios = " " * (i)
        ladrillos = "* " * (base)
        print(espacios + ladrillos)
        base -= 2
        i += 1

# piramide(base)
# piramide_invertida(base)
piramide_egipcia(base)
# piramide_egipcia_inv(base)

