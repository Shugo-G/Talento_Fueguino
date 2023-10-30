maximo = int(input("Ingrese el numero maximo a evaluar >>> "))

for i in range (0, maximo):
    if i % 2 == 0:
        print(F"El numero {i} es par")
    if i % 3 == 0:
        print(F"El numero {i} es multiplo de 3")
    if i % 5 == 0:
        print(F"El numero {i} es divisible en 5")