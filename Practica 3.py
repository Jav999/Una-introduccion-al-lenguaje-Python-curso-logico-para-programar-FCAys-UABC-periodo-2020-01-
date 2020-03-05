class Estudiante:
  #Indicamos atributos
  edad = 0 
  carrera = "Desconocida"
  universidad = "Desconocida"
  genero = "Femenino"
  
  #definimos funciones
  def festejar(self) :
    print("Festejando...")
    
  def estudiar(self, materia) :
    print("Estudiando "+  materia )
    
  def llorar(self) :
    print("Llorando...")
    
  def dormir(self) :
    print("Durmiendo...")
    
    #Ajustamos la edad
  def cambiarEdad(self, edadAlumno) :
    self.edad = edadAlumno
    print("Nueva edad", edadAlumno)
    
#Generamos un nuevo Estudiante
orlando = Estudiante()
orlando.estudiar("logica para programmacion")
#imprimimos atributo del objeto
orlando.cambiarEdad(20)
print(orlando.edad)