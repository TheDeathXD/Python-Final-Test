import time
import random

tiempo= 600

def Misiones():
   exp = random.randint(3 , 9)
   print("Mision Diaria Disponible! \n ")
   while True:
      print("1- Matar 3 Slimes || 2- Recolectar 5 Materiales || 3- Ayuda a 2 NPCs \n")
      seleccion= input("\n Escoja la mision: \n")
      if seleccion== "1":
         print("Derrotando Slimes, espere un momento..." )
         time.sleep(3)
         print("\n...1/3")
         time.sleep(3)
         print("\n...2/3")
         time.sleep(3)
         print("\n...3/3")
         time.sleep(1)
         print(f"Felicidades ha recibido {exp} de experiencia")
         print(f"Tiempo restante para la siguiente mision: {time.sleep(tiempo)}")
         time.sleep(tiempo)
      if seleccion== "2":
         print("Recolectando recursos, espere un momento..." )
         time.sleep(2)
         print("\n...1/5")
         time.sleep(2)
         print("\n...2/5")
         time.sleep(2)
         print("\n...3/5")
         time.sleep(2)
         print("\n...4/5")
         time.sleep(2)
         print("\n...5/5")
         time.sleep(1)
         print(f"Felicidades ha recibido {exp} de experiencia")
         print(f"Tiempo restante para la siguiente mision: {time.sleep(tiempo)}")
         time.sleep(tiempo)
      if seleccion== "3":
         print("Ayudando a NPCs, espere un momento..." )
         time.sleep(4)
         print("\n...1/2")
         time.sleep(4)
         print("\n...2/2")
         time.sleep(1)
         print(f"Felicidades ha recibido {exp} de experiencia")
         print(f"Tiempo restante para la siguiente mision: {time.sleep(tiempo)}")
         time.sleep(tiempo)
      return exp