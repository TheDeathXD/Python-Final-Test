import os
from Personaje import Personaje


def limpiar():
    os.system("cls")


def menu_juego():
    while True:
        print("\nMenu Principal")
        print("\n1 - Administrar Personaje")
        print("\n2 - Misiones Disponibles")
        print("\n3 - Mi Clan")
        print("\n0 - Salir")
        
        try:
            opcion = int(input("\nSeleccione una opcion : "))
            
        except:
            print("\nOpcion Invalida, intentelo de nuevo")
            
        else:
            if opcion == 1:
               while True:
                   limpiar()
                   print("\nGestionar Personaje")
            elif opcion == 2:
                print("Opcion 2")  
            elif opcion == 3:
                print("Opcion 3")  
            elif opcion == 0:
                break
 
                