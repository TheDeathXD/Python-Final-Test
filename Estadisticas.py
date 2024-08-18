class Estadisticas():
   def __init__(self, vitalidad = 0, defensa = 0, suerte = 0):
      self.vitalidad = vitalidad
      self.defensa = defensa
      self.suerte = suerte
      
   def get_vitalidad(self):
      return self.vitalidad
   def get_defensa(self):
      return self.defensa
   def get_suerte(self):
      return self.suerte
   def set_vitalidad(self, new_vitalidad):
      self.vitalidad = new_vitalidad
   def set_defensa(self, new_defensa):
      self.defensa = new_defensa
   def set_suerte(self, new_suerte):
      self.suerte = new_suerte   