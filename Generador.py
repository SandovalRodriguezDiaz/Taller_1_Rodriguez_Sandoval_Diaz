import math
import matplotlib.pylab as plt

class ondas:
    wavearray = []

    def __init__(self, frecuencia, fmuestreo, pbits, time, VP):
        self.Frecuenciam = fmuestreo
        self.Profundidadb = pbits
        self.Duracion = time
        self.Frecuencia = frecuencia
        self.size = fmuestreo * time
        self.VPbD = VP

    def sinusoidal(self):

        for i in range(0, self.size):
            #

            valores = ((10**(self.VPbD/20)*96.32))*math.sin((2*math.pi*self.Frecuencia*i)/self.Frecuenciam)
            ondas.wavearray.append(valores)

        return ondas.wavearray

    def graficar(self, array):
        plt.plot(array, color="green", linewidth=1.0, linestyle="-")
        plt.show()

class cuadrada:

    wavearray = []

    def __init__(self, frecuencia, fmuestreo, pbits, time):
        self.Frecuenciam = fmuestreo
        self.Profundidadb = pbits
        self.Duracion = time
        self.Frecuencia = frecuencia
        self.size = fmuestreo * time
    def square(self):


        for i in range(0, self.size):
            a=((4/math.pi)*((10**(self.VPbD/20)*96.32)))
            datos=0
            for j in range(0, 100):
                par=j%2
                if par:


                    valores=(1/float(j))*math.sin(((j*math.pi*self.Frecuencia*i))/self.Frecuenciam)
                    datos=datos + valores

            forma=datos*a

            cuadrada.wavearray.append(forma)

        return cuadrada.wavearray



    def graficar(self, array):
        plt.plot(array, color="red", linewidth=1.0, linestyle="-")
        plt.show()


class triangular:

    wavearray = []

    def __init__(self, frecuencia, fmuestreo, pbits, time):
        self.Frecuenciam = fmuestreo
        self.Profundidadb = pbits
        self.Duracion = time
        self.Frecuencia = frecuencia
        self.size = fmuestreo * time

    def triangulo(self):

        for i in range(0, self.size):
            a=((8/float(math.pi**2))*(10**(self.VPbD/20)*96.32))
            datos=0

            for j in range(1, 100):
                par=j%2
                if par:
                    val=(-1**((j-1)/2))/float(j**2)
                    value=val*math.sin((j*math.pi*self.Frecuencia*i)/float(self.Frecuenciam))
                    datos=datos+value
            forma=datos*a

            triangular.wavearray.append(forma)

        return triangular.wavearray



    def graficar(self, array):
        plt.plot(array, color="yellow", linewidth=1.0, linestyle="-")
        plt.show()

class sierra:

    wavearray = []

    def __init__(self, frecuencia, fmuestreo, pbits, time):
        self.Frecuenciam = fmuestreo
        self.Profundidadb = pbits
        self.Duracion = time
        self.Frecuencia = frecuencia
        self.size = fmuestreo * time

    def diente(self):

        for i in range(0, self.size):
            a=((0.5)-(1/math.pi)*(10**(self.VPbD/20)*96.32))
            datos=0
            for j in range(1, 100):
                value=(1/float(j))*math.sin((j*math.pi*self.Frecuencia*i)/self.Frecuenciam)
                datos=datos+value
            frame=datos*a
            sierra.wavearray.append(frame)

        return sierra.wavearray



    def graficar(self, array):
        plt.plot(array, color="purple", linewidth=1.0, linestyle="-")
        plt.show()