import math
import wave
import struct

class rmspico:
    nombre = input("Ingrese la direccion del archivo de audio entre comillas: ")
    Archivo = wave.open(nombre, "rb")
    #Archivo = wave.open("/Users/212equipo14/Downloads/Pycharm2/FarewellBallad.wav", "rb")
    tamano = int(Archivo.getnframes())
    tiempo= tamano/44100
    sumatoria=0
    T1=1/44100
    print "El audio tiene una duracion de: ",tiempo,"segundos."
    for i in range(0, tamano):
        DatosArray = Archivo.readframes(1)
        Datos = struct.unpack("<i", DatosArray)
        sumatoria = sumatoria + int(Datos[0])**2

    ValorRms=math.sqrt(sumatoria/tamano)
    print "El valor RMS de la senal es: ",ValorRms

    ValorpicoRms= 20*math.log10(ValorRms/(2**16))
    print "El valor pico en dBFS es: ", ValorpicoRms

    Rango=20*math.log10(2**16)
    ValorRMSDB=20*math.log(ValorRms/(Rango))
    Valorpico=max(DatosArray)
    #Picodbfs=20*math.log10(float(???)/(2**16))

    #print "El valor pico de la senal es: ",Picodbfs

    #for i in range(0, tamano):
        #DatosArray = Archivo.readframes(1)
        #Datos = struct.unpack("<i", DatosArray)

        #sumatoria = sumatoria + ((int(Datos[0])**2)*T1)

    #leq=20*math.log10((1/tiempo)*(sumatoria)/2**16)
    #print "El Leq de la senal es: ",leq






