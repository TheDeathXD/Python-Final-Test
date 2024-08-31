import time
import random

tiempo= 60


def Misiones():
   exp = random.randint(3 , 9)
   print("Mision Diaria Disponible! \n ")
   while True:
      try:
         print("1- Matar 3 Slimes || 2- Recolectar 5 Materiales || 3- Ayuda a 2 NPCs \n")
         seleccion= input("\n Escoja la mision: \n")
      except:
         print("Opcion Invalida")
         return Misiones()
      else:
         if seleccion== "1":
            print("Derrotando Slimes, espere un momento..." )
            time.sleep(3)
            print("\n1/3...")
            time.sleep(3)
            print("\n2/3...")
            time.sleep(3)
            print("\n3/3...")
            time.sleep(1)
            print(f"Felicidades ha recibido {exp} de experiencia")
            print(f"Tiempo restante para la siguiente mision: {(tiempo)} segundos")
            break
         elif seleccion== "2":
            print("Recolectando recursos, espere un momento..." )
            time.sleep(2)
            print("\n1/5...")
            time.sleep(2)
            print("\n2/5...")
            time.sleep(2)
            print("\n3/5...")
            time.sleep(2)
            print("\n4/5...")
            time.sleep(2)
            print("\n5/5...")
            time.sleep(1)
            print(f"Felicidades ha recibido {exp} de experiencia")
            print(f"Tiempo restante para la siguiente mision: {(tiempo)} segundos")
            break
         elif seleccion== "3":
            print("Ayudando a NPCs, espere un momento..." )
            time.sleep(4)
            print("\n1/2...")
            time.sleep(4)
            print("\n2/2...")
            time.sleep(1)
            print(f"Felicidades ha recibido {exp} de experiencia")
            print(f"Tiempo restante para la siguiente mision: {(tiempo)}")
            break
   return exp
   






Misiones()

