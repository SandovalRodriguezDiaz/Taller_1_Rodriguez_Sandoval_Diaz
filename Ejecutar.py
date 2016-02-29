from Generador import ondas
from Generador import cuadrada
from Generador import triangular
from Generador import sierra
from Archivar import file

def main():

    print ("-Generador de Ondas-")
    opcion = input("\n1.Sinosoidal \n2.Cuadrada \n3.Triangular \n4.Diente de Sierra \nEscoja una opcion: ")
    print ("Ingrese los siguientes datos: ")
    Tone = input("- Frecuencia del tono a generar: ")
    Time = input("-Tiempo del audio en segundos: ")
    VPdB=input("Ingrese el valor pico en dBFS: ")
    Frecuenciademuestreo = 44100
    Pbits = 16
    Name = raw_input("-Nombre del archivo a generar: ")
    Name = (Name+".wav")

    if opcion == 1:

        senal = ondas(Tone, Frecuenciademuestreo, Pbits, Time, VPdB)
        onda = senal.sinusoidal()

        doc = file(Frecuenciademuestreo, Pbits, Name)
        doc.archive(onda)

        senal.graficar(onda)

    if opcion == 2:

        senal = cuadrada(Tone, Frecuenciademuestreo, Pbits, Time, VPdB)
        onda = senal.square()

        doc = file(Frecuenciademuestreo, Pbits, Name)
        doc.archive(onda)

        senal.graficar(onda)

    if opcion == 3:

        senal = triangular(Tone, Frecuenciademuestreo, Pbits, Time, VPdB)
        onda = senal.triangulo()

        doc = file(Frecuenciademuestreo, Pbits, Name)
        doc.archive(onda)

        senal.graficar(onda)

    if opcion == 4:

        senal = sierra(Tone, Frecuenciademuestreo, Pbits, Time, VPdB)
        onda = senal.diente()

        doc = file(Frecuenciademuestreo, Pbits, Name)
        doc.archive(onda)

        senal.graficar(onda)



if __name__== "__main__":
    main()