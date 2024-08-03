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
        arma= Armas
        nivel=Level()
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
             elif profesion== 2:
              profesionfin= 'Medico'
              break
             elif profesion== 3:
              profesionfin= 'Escriba'
              break
             elif profesion== 4:
              profesionfin= 'Alquimista'
              break
             elif profesion== 5:
              profesionfin= 'Profeta'
              break
            return profesionfin
        
    def Armas(clase):
        while True:
            
            if clase== 'Mago':
                weapon= input("Confirme su arma para continuar")
                arma= "Baston de Madera"
                print("Ha obtenido un "+ arma)
                break
            elif clase== 'Brujo':
                weapon= input("Confirme su arma para continuar")
                arma= "Baston de Madera"
                print("Ha obtenido un "+ arma) 
                break
            elif clase== 'Guerrero':
             try:
                weapon= input("Escoja su arma")
                print ('1-Espada de hierro | 2-Mandoble | 3-Maza')
             except:
              print("Error escoja nuevamente")
             else:
                if weapon== 1:
                 arma=='Espada de hierro' 
                 print("Ha obtenido un "+ arma)
                 break
                elif weapon== 2:
                 arma=='Mandoble' 
                 print("Ha obtenido un "+ arma)
                 break
                elif weapon== 3:
                 arma=='Maza' 
                 print("Ha obtenido un "+ arma)
                 break
            elif clase== 'Paladin':
             try:
                weapon= input("Escoja su arma")
                print ('1-Espada de hierro | 2-Mandoble | 3-Maza')
             except:
              print("Error escoja nuevamente")
             else:
                if weapon== 1:
                 arma=='Espada de hierro' 
                 print("Ha obtenido un "+ arma)
                 break
                elif weapon== 2:
                 arma=='Mandoble' 
                 print("Ha obtenido un "+ arma)
                 break
                elif weapon== 3:
                 arma=='Maza' 
                 print("Ha obtenido un "+ arma)
                 break   
            if clase== 'Arquero':
                weapon= input("Confirme su arma para continuar")
                arma= "Arco de Madera"
                print("Ha obtenido un "+ arma)
                break   
            if clase== 'Picaro':
                weapon= input("Confirme su arma para continuar")
                arma= "Cuchillo de hierro"
                print("Ha obtenido un "+ arma)
                break  
            if clase== 'Monje':
                print("No obtienes armas pero pegas mas fuerte a puño limpio")
                weapon= input("Confirme para continuar")
                arma= None
                print("Ha mejorado su daño con los puños")
                break 
            if clase== 'Virgen':
                print("Desconozco la razon de por que escogeria esta clase pero weno")
                weapon= input("Confirme su arma para continuar")
                arma= "Palo de Madera"
                print("Ha obtenido un "+ arma)
                break 
            return arma 

    def Level():
     nivel = 1
     exp_requerida = nivel * 10
     exp_obtenida = 0 
     while True: 
      if exp_obtenida == exp_requerida:  
       nivel= nivel+1
       exp_obtenida= 0
       print(f"Felicidades ha subido a Nivel {nivel}")
      elif exp_obtenida > exp_requerida :
       nivel= nivel+1
       exp_obtenida= 0
       print(f"Felicidades ha subido a Nivel {nivel}")
      else:
          continue
      return nivel
         