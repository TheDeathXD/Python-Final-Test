from Personaje import Personaje
from Estadisticas import Estadisticas
import time
import main

clasefin = 'Base'
puntos_hab = 0
nivel = 0
arma = None
def menu_inicio():
   print("\nBienvenido a Tragones y Mazmorras!")
   print("\n1 - Iniciar Juego")
   print("\n0 - Salir")
   try:
      opcion = int(input("\nSeleccione una opcion : "))       
   except:
      print("\nOpcion Invalida, intentelo de nuevo")
      menu_inicio()
   else:
      if(opcion == 0):
         time.sleep(2)
         main.limpiar()
         print("Saliendo del juego... ")
         time.sleep(3)
         exit
      elif(opcion == 1):
         print("\nCREACION DEL PERSONAJE ")
         time.sleep(0.8)
         nombre = input("\nIngrese su nombre: ")
         time.sleep(0.5)
         edad = input("\nIngrese la edad: ")
         time.sleep(0.5)
         clase = Clases()
         time.sleep(1)
         profesion = Profesion()
         time.sleep(1)
         Level()
         stats = Stats_Base()
         
         with open("personaje.txt",'w',encoding='UTF-8') as datos:
            datos.write("\n Hoja de Personaje: \n")
            datos.write(f"{nombre}\n")
            datos.write(f"{edad} años \n")
            datos.write(f"{clasefin}\n")
            datos.write(f"{profesion}\n")
            datos.write(f"{nivel}\n")
            datos.write(f"{stats}\n")
         with open("personaje.txt",'r',encoding='UTF-8') as datos:
            datos.read()
         time.sleep(0.5)   
         opcion1 = input("\nPresione cualquier tecla para aceptar o escriba 'No' para regresar al menú y deshacer el personaje: ")
         if(opcion1 == "No" ):
            return menu_inicio()
         else:
            main.limpiar()
            print("Bienvenido a Tragones y Mazmorras \nQue la Aventura comience! ")
            time.sleep(2)
            print("Generando terreno... ")
            time.sleep(3)
            print("Generando enemigos... ")
            time.sleep(2)
            print("Generando objetos...")

def Clases():
   global clasefin
   global arma
   while True:
      print("Clases: 1-Mago | 2-Paladin | 3- Guerrero | 4-Picaro | 5-Arquero | 6-Brujo | 7-Monje | 8-Virgen")
      try:
         clase = input("Escoja una clase: ")
      except:
         print("Opcion Invalida")
      else:
         if clase == "1":
            clasefin= 'Mago'
            print("Bienvenido sea erudito arcano y conocedor de toda magia")
            time.sleep(0.5)
            arma = "Baston de Madera"
            print("Ha obtenido un "+ arma)
            daño_vel_arma = (6, 1)
            break
         elif clase == "2":
            clasefin= 'Paladin'
            print("Me inclino ante usted y su honor caballero sagrado")
            time.sleep(0.5)
            arma = "Espada de Hierro"
            print("Ha obtenido una "+ arma)
            daño_vel_arma = (8, 1)
            break
         elif clase == "3":
            clasefin= 'Guerrero'
            print("Que su gran fortaleza sea la suficiente para su causa valiente guerrero")
            time.sleep(0.5)
            arma = "Mandoble"
            print("Ha obtenido un "+ arma)
            daño_vel_arma = (11, 0.7)
            break
         elif clase == "4":
            clasefin= 'Picaro'
            print("Es hora de desvanecerse y ser uno con las sombras")
            time.sleep(0.5)
            arma = "Daga de Hierro"
            print("Ha obtenido una "+ arma)
            daño_vel_arma = (5, 1.5)
            break
         elif clase == "5":
            clasefin= 'Arquero'
            print("Preparado para poner esas flechas sobre sus enemigos mi estimado francotirador")
            time.sleep(0.5)
            arma = "Arco de Madera"
            print("Ha obtenido un "+ arma)
            daño_vel_arma = (6, 1.2)
            break
         elif clase == "6":
            clasefin= 'Brujo'
            print("Sin importar los motivos, demuestrale al mundo la capacidad de tu poder")
            time.sleep(0.5)
            arma = "Baston de Madera"
            print("Ha obtenido un "+ arma)
            daño_vel_arma = (8, 0.8)
            break
         elif clase == "7":
            clasefin= 'Monje'
            print("Demuestrale al mundo que con los puños tienes la capacidad de derrotar hasta dragones")
            time.sleep(0.5)
            arma = "Puños"
            print(f"Sus {arma} han sido mejorados")
            daño_vel_arma = (4, 2)
            break
         elif clase == "8":
            clasefin= 'Gran Sabio'    
            print("Ehh si escogistes esto es o porque eres un troll o porque le sabes a los easter-eggs :b")
            time.sleep(0.5)
            arma = "Palo de Madera"
            print("Ha obtenido un "+ arma)
            daño_vel_arma = (4, 1.5)
            break
         else:
            print("Opcion no Valida")
            return Clases()
   return clasefin, arma, daño_vel_arma

def Profesion():
   while True:
      print("Profesiones: 1- Herrero | 2-Medico | 3- Escriba | 4- Alquimista | 5- Profeta ")      
      try:
         profesion= input("Escoja una profesion: ")
      except:
         print("Opcion Invalida")
         return Profesion()
      else:
         if profesion==  "1":
            profesionfin= 'Herrero'
            print("Ha adquirido la habilidad de forjar armas")
            break
         elif profesion== "2":
            profesionfin= 'Medico'
            print("Ha adquirido la habilidad de crear medicinas")
            break
         elif profesion== "3":
            profesionfin= 'Escriba'
            print("Ha adquirido la habilidad de leer textos antiguos")
            break
         elif profesion== "4":
            profesionfin= 'Alquimista'
            print("Ha adquirido la habilidad de crear pociones")
            break
         elif profesion== "5":
            profesionfin= 'Profeta'
            print("Ha adquirido la capacidad de predecir movimientos futuros")
            break
   return profesionfin

def Level():
   global nivel
   global puntos_hab
   nivel = 1
   exp_requerida = nivel * 10
   exp_obtenida = 0
   if exp_obtenida == exp_requerida or exp_obtenida > exp_requerida :  
      nivel= nivel+1
      exp_obtenida= 0
      puntos_hab= puntos_hab + 3 + nivel/5
      if(clasefin== 'Gran Sabio'):
         puntos_hab= puntos_hab + 4 + nivel/5
         print(f"Felicidades ha subido a Nivel {nivel}")


def Stats_Base():
   class Bases(Estadisticas()):
      if(clasefin == 'Mago'):
         general_stats = Estadisticas(5,2,3)
      elif(clasefin == 'Paladin'):
         general_stats = Estadisticas(6,4,0)
      elif(clasefin == 'Guerrero'):
         general_stats = Estadisticas(8,2,0)
      elif(clasefin == 'Brujo'):
         general_stats = Estadisticas(4,2,4)
      elif(clasefin == 'Arquero'):
         general_stats = Estadisticas(5,1,4)
      elif(clasefin == 'Picaro'):
         general_stats = Estadisticas(3,2,5)
      elif(clasefin == 'Gran Sabio'):
         general_stats = Estadisticas(3,1,6)




def LevelUp(estadistica):
   while(puntos_hab>0):
      estadistica = estadistica+1
      puntos_hab = puntos_hab - 1
   return estadistica


menu_inicio()