
class Serie:

    def __init__(self, titulo = "", numTemp = 3, creador = "", genero = ""):

        self.titulo = titulo
        self.numTemp = numTemp
        self.entregado = False
        self.genero = genero
        self.creador = creador

    def entregar(self):
        self.entregado = True

    def getCreador(self):
        return self.creador

    def getNumTemp(self):
        return self.numTemp

    def getCreador(self):
        return self.creador

    def getGenero(self):
        return self.genero

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setNumTemp(self, numTemp):
        self.numTemp = numTemp

    def setCreador(self, creador):
        self.creador = creador

    def setGenero(self, genero):
        self.genero = genero

class VideoJuego:

    def __init__(self, titulo = "", horasEst = 10, genero = "", comp = ""):
        self.titulo = titulo
        self.horasEst = horasEst
        self.entregado = False
        self.genero = genero
        self.compania = comp

    def entregar(self):
        self.entregado = True

    def getTitulo(self):
        return self.titulo

    def getHorasEst(self):
        return self.horasEst

    def getGenero(self):
        return self.genero

    def getComp(self):
        return self.comp

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setHorasEst(self, horasEst):
        self.horasEst = horasEst

    def setGenero(self, genero):
        self.genero = genero

    def setComp(self, comp):
        self.comp = comp

series = []
serie1 = Serie("Juego de tronos",9,"HBO","Acción y aventura")
serie1.entregar()
serie2 = Serie("Vikingos",7,"Netflix","Acción y aventura")
serie3 = Serie("Seal Team",5, "Netflix","Belico")
serie3.entregar()
serie4 = Serie("El Internado",10, "Atresmedia","Thriller")
serie4.entregar()
serie5 = Serie("Nosferatu",666, "Nosferatu","NOSFERATU")

series.append(serie1)
series.append(serie2)
series.append(serie3)
series.append(serie4)
series.append(serie5)

contSeries = 0

for i in range(0,5):
    if(series[i].entregado == True):
        contSeries += 1

print("Hay "+str(contSeries)+" series entregadas.")

videojuegos = []
videojuegos1 = VideoJuego("Conan Exiles",180,"MMO","Unreal")
videojuegos2 = VideoJuego("FALLOUT4",200,"Accion","Bthesda")
videojuegos2.entregar()
videojuegos3 = VideoJuego("GTAV",200,"Accion","Rockstar Games")
videojuegos3.entregar()
videojuegos4 = VideoJuego("ARMA3",100,"Simulador Belico","Bohemia Interactive")
videojuegos5 = VideoJuego("Battlefield4",120,"Guerra","EA")

videojuegos.append(videojuegos1)
videojuegos.append(videojuegos2)
videojuegos.append(videojuegos3)
videojuegos.append(videojuegos4)
videojuegos.append(videojuegos5)

contJuegos = 0

for i in range(0,5):
    if videojuegos[i].entregado == True:
        contJuegos += 1

print("Hay "+str(contJuegos)+" videojuegos entregados.")

contTemp = 0
serie = ""

for i in range(0,5):
    if series[i].numTemp >= contTemp:
        contTemp = series[i].numTemp
        serie = series[i].titulo

print("La serie con más temporadas es \"" + serie + "\" con " + str(contTemp) + " temporadas.")

contJuego = 0
juego = ""

for i in range(0,5):
    if videojuegos[i].horasEst >= contJuego:
        contJuego = videojuegos[i].horasEst
        juego = videojuegos[i].titulo

print("El videojuego más largo es \"" + juego + "\" con " +  str(contJuego) + " horas de juego.")
