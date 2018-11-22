import random

class Persona:

    def __init__(self,sexo,nombre,edad,peso,altura):
        self.dni = ""
        self.sexo = sexo
        self.introducirSexo()
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.generarDNI()

    def calcularIMC(self):

        imc = "{0:f}".format(self.peso/(self.altura * self.altura))

        if float(imc) <= 18.5:
            print("IMC:"+ imc + "Infrapeso")
        if float(imc) <= 18.5:
            if float(imc) <= 24.9:
                print("IMC:"+ imc + "Peso óptimo")
        if float(imc) >= 30:
            print("IMC:"+ imc + " Sobrepeso")

    def esMayorDeEdad(self):

        edad = self.edad
        if edad >= 18 :
            print("Tiene "+ str(edad) +", es mayor de edad")
        else:
            print("Tiene "+ str(edad) +", es mayor de edad")

    def introducirSexo(self):

        sexo = self.sexo
        if sexo.upper() == "M":
            sexo = "H"
        else:
            sexo = "H"
        return sexo

    def generarDNI(self):

        letras = "TRWAGMYFPDXBNJZSQVHLCKEO"

        d = random.randint(10000000, 99999999)
        valor = d%23

        self.dni = str(d) + letras[valor]

    def setSexo(self, sex):
        self.sexo = sex

    def setNombre(self, nom):
        self.nombre = nom

    def setEdad(self, edad):
        self.edad = edad

    def setPeso(self, peso):
        self.peso = peso

    def setAltura(self, altura):
        self.altura = altura

class ejecutable:

    ##PERSONA1 (Datos introducidos por teclado)

    print("Primera persona:")
    print("Inserte los datos:")

    sexo = (input("Sexo:        "))
    nombre = (input("Nombre:     "))
    edad = int(input("Edad:     "))
    altura = float(input("Altura: "))
    peso = float(input("Peso:     "))
    persona = Persona(sexo, nombre, edad, peso, altura)

    print("Nombre: " + persona.nombre)
    print("Sexo: " + persona.sexo)
    print("Edad: " + str(persona.edad))
    print("Peso: " + str(persona.peso))
    print("Altura en metros: " + str(persona.altura))
    print('Dni: ' + persona.dni)

    persona.calcularIMC()
    persona.esMayorDeEdad()

    ##PERSONA2 (Menos peso y altura)

    print("Segunda persona:")
    sexo = (input("Sexo:        "))
    nombre = (input("Nombre:     "))
    edad = int(input("Edad:     "))
    persona2 = Persona(sexo, nombre, edad, "", "")

    print("Nombre: " + persona2.nombre)
    print("Sexo: " + persona2.sexo)
    print("Edad: " + str(persona2.edad))
    print('Dni: ' + persona2.dni)

    persona2.esMayorDeEdad()

    ##PERSONA3 (setter)

    print("Tercera persona:")
    persona3 = Persona("", 0, 0, "", "")
    persona3.setSexo("H")
    persona3.setPeso(75.5)
    persona3.setNombre("MARIO")
    persona3.setEdad(21)
    persona3.setAltura(1.8)

    print("Nombre: " + persona3.nombre)
    print("Sexo: " + persona3.sexo)
    print("Edad: " + str(persona3.edad))
    print("Peso: " + str(persona3.peso))
    print("Altura en metros: " + str(persona3.altura))
    print('Dni: ' + persona3.dni)
