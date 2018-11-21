#Autor Patricio Mondragón


import matplotlib.pyplot as plot

#4. Buscar los equipos que tienen mal reportado.

def buscarEquiposcConError(nombredelArchivo):
    entrada= open(nombredelArchivo,"r")
    equipos = []
    entrada.readline()#titulo1
    entrada.readline()#titulo2
    for linea in entrada:
        datos = linea.split("&")#veracruz, "16"]
        equipo = datos[0]
        jg = int(datos[2])
        je = int(datos[3])
        puntosreportados = int(datos[8])
        puntos = jg*3+je*1
        if puntos != puntosreportados:
            equipos.append(equipo)


    entrada.close()
    return equipos

def graficarPuntos(nombreArchivo):
    entrada = open(nombreArchivo,"r")
    entrada.readline()  # titulo1
    entrada.readline()  # titulo2

    listaEquipos = []
    listaPuntos = []
    for linea in entrada:
        datos = linea.split("&")
        listaEquipos.append(datos[0])
        listaPuntos.append(int(datos[8]))

    plot.plot(listaEquipos,listaPuntos)
    plot.show()
    entrada.close()

def mostrarlista(nombreArchivo):
    entrada = open(nombreArchivo,"r")
    listaequipos = []
    entrada.readline()
    entrada.readline()
    for linea in entrada:
        datos = linea.split("&")
        equipo = datos[0]
        pg = datos[2]
        listaequipos.append((equipo,pg))
    return listaequipos



def main():
    errores= buscarEquiposcConError("ligaMx")
    print(errores)
    graficarPuntos("ligaMx")
    listaEquiposConPg = mostrarlista("ligaMx")
    print(listaEquiposConPg)


main()