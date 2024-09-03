class Inventario:
   def __init__(self):
      self.item= []
   def Add_Inv(self, item):
      self.item.append(item)
      print(f"{item} ha sido añadido al inventario")
      self.Actualizar_Inv()

   def Delete_Inv(self, item):
      if item in self.item:
         self.item.remove(item)
         print(f"{item} ha sido eliminado del inventario ")
         self.Actualizar_Inv()
      else:
         print(f"{item} no existe en el inventario ")

   def Ver_Inv(self):
      if self.item:
         print("Inventario: \n")
         for item in self.item:
            print(f"- {item}")
      else:
         print("El inventario esta vacio")

   def Actualizar_Inv(self):
      with open('Escritorio\\inventario','w',encoding='UTF-8') as inventario:
         for i in self.item:
            inventario.write(f"{i}\n")
      print("Inventario Actualizado")

   def Cargar_Inv(self):
      try:
         with open('Escritorio\\inventario.txt', 'r', encoding= 'UTF-8') as inventario:
            self.item= [linea.strip() for linea in inventario]
         print("Inventario Cargado")
      except FileNotFoundError:
         print("No se encontro el archivo del inventario")