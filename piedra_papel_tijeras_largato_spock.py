# Piedra, Papel, Tijera, Largarto, Spock

# Las tijeras cortan el papel.      ✂️ > ✋
# El papel cubre la piedra.         ✋ > ✊
# La piedra aplasta el lagarto.     ✊ > 🦎
# El lagarto envenena a Spock.      🦎 > 🖖
# Spock aplasta las tijeras.        🖖 > ✂️
# Las tijeras decapitan el lagarto. ✂️ > 🦎
# El lagarto se come el papel.      🦎 > ✋
# El papel refuta a Spock.          ✋ > 🖖
# Spock vaporiza la piedra.         🖖 > ✊
# La piedra aplasta a las tijeras.  ✊ > ✂️

import random

# opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras", 4: "Lagarto", 5: "Spock"}

print("""
        Piedra  ✊: 1
        Papel   ✋: 2
        Tijera  ✂️: 3
        Lagarto 🦎: 4
        Spock   🖖: 5
      """)

def juego(): 
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras", 4: "Lagarto", 5: "Spock"}
    gana_contra = ()
    
    opcion_compu = opciones[random.randint(1, 5)]
    print(opcion_compu)

    opcion_jugador = opciones.get(int(input("Elije tu opción: ")),'error')

    if opcion_jugador not in opciones.values():
        print("Opción no valida, elije otra.")
        return juego()
    
    print(F"Tu opcion fué: {opcion_jugador}")
    print(F"La opcion de la compu fue: {opcion_compu}")

    if opcion_jugador == opcion_compu:
        print("EMPATE")
        return
    elif opcion_jugador == "Piedra": gana_contra = ("Tijeras", "Lagarto")
    elif opcion_jugador == "Papel": gana_contra = ("Piedra", "Spock")
    elif opcion_jugador == "Tijeras": gana_contra = ("Papel", "Lagarto")
    elif opcion_jugador == "Lagarto": gana_contra = ("Papel", "Spock")
    elif opcion_jugador == "Spock": gana_contra = ("Tijeras", "Piedra")

    if opcion_compu in gana_contra:
        print("GANASTE")
    else:
        print("PERDISTE")
 
juego()

