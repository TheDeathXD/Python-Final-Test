import random

filas = 4
columnas = 4
pos_enemigos=3
mazmorra = [['' for i in range(columnas)]for i in range(filas)]
player_position= [0 , 0]
mazmorra[player_position[0]][player_position[1]]= 'J'
for i in range(pos_enemigos):
   while True:
      posicion_enemiga=[random.randint(0, filas-1), random.randint(0, columnas-1)]
      if mazmorra[posicion_enemiga[0], posicion_enemiga[1]]== "":
         mazmorra[posicion_enemiga[0], posicion_enemiga[1]]= "E"
      break


def Crear_Mazmorra():
   for fila in mazmorra:
      print(''.join(fila))
   print()


def Mov_jugador(direccion):
   new_pos = player_position.copy()
   if direccion ==  'w' and player_position[0]> 0:
      new_pos[0] = new_pos - 1
   elif direccion == 'a' and player_position[0]>filas-1:
      new_pos[0] = new_pos + 1
   elif direccion == 's' and player_position[1]> 0:
      new_pos[0] = new_pos - 1
   elif direccion == 'd' and player_position[1]> columnas-1:
      new_pos[0] = new_pos + 1
   if mazmorra[new_pos[0], new_pos[1]]== '':
      mazmorra[player_position[0], player_position[1]] == ''
      player_position[0], player_position[1]= new_pos
      mazmorra[player_position[0], player_position[1]]= 'J'