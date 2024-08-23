from Personaje import Personaje
from Estadisticas import Estadisticas
import time
import main
clasefin = 'Base'
puntos_hab = 0

def menu_inicio():
   print("\nBienvenido a Tragones y Mazmorras")
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
         print("Crear Personaje")
         nombre = input("Nombre de su Personaje: ")
         time.sleep(0.5)
         edad = input("Ingrese la edad: ")
         time.sleep(0.5)
         clase = Clases()
         time.sleep(1)
         profesion = Profesion()
         time.sleep(1)
         armafin = Armas()
         time.sleep(1)
         nivel = Level(nivel)
         stats = Stats_Base()
         print(f"\nEste es su personaje: \nNombre: {nombre} \nEdad: {edad} años \nClase: {clase} \nProfesion: {profesion} \nArma: {armafin} \nNivel: {nivel} \nStats: \n{stats} ")
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
            break
         elif clase == "2":
            clasefin= 'Paladin'
            print("Me inclino ante usted y su honor caballero sagrado")
            break
         elif clase == "3":
            clasefin= 'Guerrero'
            print("Que su gran fortaleza sea la suficiente para su causa valiente guerrero")
            break
         elif clase == "4":
            clasefin= 'Picaro'
            print("Es hora de desvanecerse y ser uno con las sombras")
            break
         elif clase == "5":
            clasefin= 'Arquero'
            print("Preparado para poner esas flechas sobre sus enemigos mi estimado francotirador")
            break
         elif clase == "6":
            clasefin= 'Brujo'
            print("Sin importar los motivos, demuestrale al mundo la capacidad de tu poder")
            break
         elif clase == "7":
            clasefin= 'Monje'
            print("Demuestrale al mundo que con los puños tienes la capacidad de derrotar hasta dragones")
            break
         elif clase == "8":
            clasefin= 'Gran Sabio'    
            print("Ehh si escogistes esto es o porque eres un troll o porque le sabes a los easter-eggs :b")
            break
         else:
            print("Opcion no Valida")
            return Clases()
   return clasefin

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




def Armas():
   try:
      print("Su arma correspondiente le será entregada")
      time.sleep(2)
   except:
      print("Error")
   else:
      if clasefin== 'Mago' or clasefin== 'Brujo':
         arma = "Baston de Madera"
         print("Ha obtenido un "+ arma)
         daño_arma = 6
      elif clasefin== 'Guerrero' or clasefin== 'Paladin':
         print ('1-Espada de hierro | 2-Mandoble | 3-Maza')
         weapon= input("Escoja su arma: ")
         if weapon== "1":
            arma = 'Espada de hierro' 
            print("Ha obtenido una "+ arma)
            daño_arma = 8
         elif weapon== "2":
            arma = 'Mandoble' 
            print("Ha obtenido un "+ arma)
            daño_arma = 11
         elif weapon== "3":
            arma = 'Maza' 
            print("Ha obtenido una "+ arma)
            daño_arma = 9
      elif clasefin== 'Arquero':
         arma = "Arco de Madera"
         print("Ha obtenido un "+ arma)
         daño_arma = 6   
      elif clasefin== 'Picaro':
         arma = "Cuchillo de hierro"
         print("Ha obtenido un "+ arma)
         daño_arma = 5
      elif clasefin== 'Monje':
         print("No obtienes armas pero pegas mas fuerte a puño limpio")
         arma = "Puños"
         print("Ha mejorado su daño con los puños")
         daño_arma = 5
      elif clasefin== 'Gran Sabio':
         print("Desconozco la razon de por que escogeria esta clase pero weno")
         arma = "Palo de Madera"
         print("Ha obtenido un "+ arma)
         daño_arma = 4


def Level(nivel):
   nivel=1
   exp_requerida = nivel * 10
   exp_obtenida = 0
   if exp_obtenida == exp_requerida:  
      nivel= nivel+1
      exp_obtenida= 0
      puntos_hab= puntos_hab + 3 + nivel/5
      if(clasefin== 'Gran Sabio'):
         puntos_hab= puntos_hab + 4 + nivel/5
         print(f"Felicidades ha subido a Nivel {nivel}")
   elif exp_obtenida > exp_requerida :
      nivel= nivel+1
      exp_obtenida= 0
      if(clasefin== 'Gran Sabio'):
         puntos_hab= puntos_hab + 4 + nivel/5
         print(f"Felicidades ha subido a Nivel {nivel}")


def Stats_Base():
   class Bases(Estadisticas): 
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