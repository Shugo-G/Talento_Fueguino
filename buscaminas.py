import random

# Buscaminas
# Pedir al usuario la cantidad de filas
# Pedir al usuario la cantidad de columnas
# Matriz fila x columnas
# random.randint(0, 1)
# 0 -> libre
# 1 -> bomba
#Mostrar el tablero

# Variables solicitadas al usuario
filas = int(input("Ingrese cantidad de filas: "))
columnas = int(input("Ingrese cantidad de columnas: "))


# buscamina = [[random.randint(0,1) for i in range(columnas)] for i in range(filas)]
buscamina = []
tablero_progreso = [["⬜" for i in range(columnas)] for i in range(filas)]

# Genero tablero de juego
for f in range(0, filas):
  buscamina.append([])
  for c in range(0, columnas):
    buscamina[f].append(random.choice(["💣", "⬜"]))

def contar_minas_y_espacios(buscamina):
  minas = 0
  espacios = 0
  for f in range(0, len(buscamina)):
    for c in range(0, len(buscamina[f])):
      if buscamina[f][c] == "💣":
        minas += 1
      if buscamina[f][c] == "⬜":
        espacios += 1
  return minas, espacios
    
# Dibuja tablero pasado por parámetro
def pintar_tablero(buscamina):
  for row in buscamina:
    print("".join(map(str, row)))

# Actualiza y valida la posición
def actualizar_posicion():
  posicion = int(input("Elegir fila: ")), int(input("Elegir columna: "))
  pos_y, pos_x = posicion
  filas_permitidas = [i for i in range(filas)]
  columnas_permitidas = [i for i in range(columnas)]

  print(posicion)

  if (pos_y in filas_permitidas) and (pos_x in columnas_permitidas):
    return posicion
  else:
    print("posicion no válida. Elija nuevamente")
    return actualizar_posicion()

# Actualiza el tablero del jugador y las variables según el elemento en la casilla
def chequear_casilla(buscamina, tablero_progreso, posicion):
  pos_y, pos_x = posicion
  global minas, vidas, espacios

  if tablero_progreso[pos_y][pos_x] in ("💥", "🟩"):
    print("Esta casilla ya fue seleccionada")                                  
  elif buscamina[pos_y][pos_x] == "💣":
    minas -= 1
    vidas -= 1
    tablero_progreso[pos_y][pos_x] = "💥"
  elif buscamina[pos_y][pos_x] == "⬜":
    tablero_progreso[pos_y][pos_x] = "🟩"
    espacios -= 1


# pintar_tablero(buscamina)
# print('/n')
pintar_tablero(tablero_progreso)
minas, espacios = contar_minas_y_espacios(buscamina)
vidas = 5
gana = False
pierde = False


print("¡¡BUSCAMINAS!!")

while not(gana) and not(pierde):
  print("-" * 40)
  print(f"Vidas restantes: {vidas} --- Minas restantes: {minas} --- Espacios: {espacios}")

  posicion = actualizar_posicion()
  chequear_casilla(buscamina, tablero_progreso, posicion)

  if espacios == 0:
    gana = True
  if minas == 0 or vidas == 0:
    pierde = True

  pintar_tablero(tablero_progreso)

if gana:
  print("""
        🏆 ¡¡¡Felicidades ganaste el juego!! 🏆

        """)
if pierde:
  print("""
        ☠️ ☠️ ☠️  GAME OVER ☠️ ☠️ ☠️
        
        """)

pintar_tablero(buscamina)