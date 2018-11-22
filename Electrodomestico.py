
class Electrodomestico:

    def __init__(self, precioBase, color, consumoEnergetico, peso):
        self.precioBase = precioBase
        self.color = color
        self.consumoEnergetico = consumoEnergetico
        self.peso = peso
        self.comprobarConsumoEnergetico()
        self.comprobarColor()

    def comprobarConsumoEnergetico(self):

        consumo = self.consumoEnergetico

        if consumo.upper() == "A":
            self.consumoEnergetico = "A"
        elif consumo.upper() == "B":
            self.consumoEnergetico = "B"
        elif consumo.upper() == "C":
            self.consumoEnergetico = "C"
        elif consumo.upper() == "D":
            self.consumoEnergetico = "D"
        elif consumo.upper() == "E":
            self.consumoEnergetico = "E"
        else:
            self.consumoEnergetico = "F"

        return self.consumoEnergetico

    def comprobarColor(self):

        color = self.color

        if color.upper() == "NEGRO":
            self.color = "NEGRO"
        elif color.upper() == "ROJO":
            self.color = "ROJO"
        elif color.upper() == "AZUL":
            self.color = "AZUL"
        elif color.upper() == "GRIS":
            self.color = "GRIS"
        else:
            self.color = "BLANCO"

        return self.color

    def getPrecio(self):
        return self.precioBase

    def getColor(self):
        return self.color
    def getConsumoEnergetico(self):
        return self.consumoEnergetico
    def getPeso(self):
        return self.peso

    def precioFinal(self):

        if self.consumoEnergetico.upper() == "A":
            self.precioBase = self.precioBase + 100
        elif self.consumoEnergetico.upper() == "B":
            self.precioBase = self.precioBase + 80
        elif self.consumoEnergetico.upper() == "C":
            self.precioBase = self.precioBase + 60
        elif self.consumoEnergetico.upper() == "D":
            self.precioBase = self.precioBase + 50
        elif self.consumoEnergetico.upper() == "E":
            self.precioBase = self.precioBase + 30
        else:
            self.precioBase = self.precioBase + 10

        if self.peso >= 0 | self.peso <= 19:
            self.precioBase = self.precioBase + 10
        elif self.peso >= 20 | self.peso <= 49:
            self.precioBase = self.precioBase + 50
        elif self.peso >= 50 | self.peso <= 79:
            self.precioBase = self.precioBase + 80
        else:
            self.precioBase = self.precioBase + 100

        return self.precioBase


class Lavadora(Electrodomestico):

    def __init__(self, carga, color, consumo, peso):
        self.carga = carga
        super().__init__(self.precioBase, color, consumo, peso)

    def getCarga(self):
        return self.carga

    def precioFinal(self):

        if self.carga > 30:
            self.precioBase = self.precioBase + 50
        return self.precioBase

class Television(Electrodomestico):

    def __init__(self, resolucion, fourk, color, consumo, peso):
        super().__init__(precio, color, consumo, peso)
        self.resolucion = resolucion
        self.fourk = fourk

    def getResolucion(self):
        return self.resolucion
    def getFourK(self):
        return self.fourk

    def precioFinal(self):

        if self.resolucion > 40:
            self.precioBase = self.precioBase * 1.3
        if self.fourk == True:
            self.precioBase = self.precioBase * 1.5

        return self.precioBase

e = Electrodomestico(200, "ROJO", "A", 90)
e1 = Electrodomestico(500, "BLANCO", "E", 200)
e2 = Electrodomestico(600, "NEGRO", "D", 150)
l = Lavadora(10, "", 100, 90)
l1 = Lavadora(25, "GRIS", 150, 100)
l2 = Lavadora(30, "AZUL", 220, 150)
t1 = Television(1080, 600, False, "NEGRO", 90, 10)
t2 = Television(2080, 1000, True, "BLANCO", 100, 12)
t3 = Television(1920, 800, True, "GRIS", 80, 5)
List = [e, e1, e2, l, l1, l2, t, t1, t2, t3]

for i in List[0:3]:
    precio = i.precioFinal()
    print(precio)
    total = total + precio
    print("Electrodomésticos: " + str(total))

for i in List[3:5]:
    precio = i.precioFinal()
    print(precio)
    total = total + precio
    print("Lavadoras: " + str(total))

for i in List[6:]:
    precio = i.precioFinal()
    print(precio)
    total = total + precio
    print("Televisiones: " + str(total))
