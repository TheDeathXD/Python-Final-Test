from Personaje import Personaje

def menu_inicio():
    print("\nBienvenido a Tragones y Mazmorras")
    print("\n1 - Iniciar Juego")
    print("\n0 - Salir")
    
    try:
            opcion = int(input("\nSeleccione una opcion : "))
            
    except:
            print("\nOpcion Invalida, intentelo de nuevo")
            
    else:
        print("Crear Personaje")
        nombre = input("Nombre de su Personaje: ")
        edad = input("Ingrese la edad: ")
        clase= Clases()
        profesion= Profesion()
        
    def Clases():
        while True:
            print("Clases: 1-Mago | 2-Paladin | 3- Guerrero | 4-Picaro | 5-Arquero | 6-Brujo | 7-Monje | 8-Virgen")
            try:
                clase= input("Escoja una clase")
            except:
                print("Opcion Invalida")
            else:
             if clase== 1:
              clasefin= 'Mago'
              break
             elif clase== 2:
              clasefin= 'Paladin'
              break
             elif clase== 3:
              clasefin= 'Guerrero'
              break
             elif clase== 4:
              clasefin= 'Picaro'
              break
             elif clase== 5:
              clasefin= 'Arquero'
              break
             elif clase== 6:
              clasefin= 'Brujo'
              break
             elif clase== 7:
              clasefin= 'Monje'
              break
             elif clase== 8:
              clasefin= 'Gran Sabio'    
              break
             else:
              print("Opcion no Valida")
             
             return clasefin
        
    def Profesion():
        while True:
            print("Profesiones: 1- Herrero | 2-Medico | 3- Escriba | 4= Alquimista | 5- Profeta ")
            
            try:
                profesion= input("Escoja una profesion")
            except:
                print("Opcion Invalida")
            else:
             if profesion== 1:
              profesionfin= 'Herrero'
              break
             elif clase== 2:
              profesionfin= 'Medico'
              break
             elif clase== 3:
              profesionfin= 'Escriba'
              break
             elif clase== 4:
              profesionfin= 'Alquimista'
              break
             elif clase== 5:
              profesionfin= 'Profeta'
              break
            return profesion
        
    def Arma(clase):
        while True:
            
         if clase== 'Mago':
          arma= "Baston de Madera"
          print("Ha obtenido un "+ arma)
         elif clase== 'Brujo':
          arma= "Baston de Madera"
          print("Ha obtenido un "+ arma) 
          
            
        
        
        
    