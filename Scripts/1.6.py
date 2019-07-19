
#Copyright <2016> Noel Cabañas
#Licensed under the Apache License, version 2.0. See LICENSE for details.

#!/usr/bin/env python
# -*- coding: utf-8


########################################
#1.6.py                            #
#Programa creado por Noel Cabañas      #
#Febrero de 2016                       #
#Nota: para mayores detalles           #
#comunicarse al correo                 #
#e-mail: noel-102@hotmail.com          #
########################################


#######################################
#1.6.py                                #
#Scritp created by Noel Cabañas        #
#Febrero de 2016                       #
#Note: It is an open-source, that can be#
#used under LICENSE.                    #
#e-mail: ncabanas@iibiomedicas.unam.mx  #
########################################


##This is the main script to identify the repeat sequences  in the mitogenomes
##You need to run the program in the same directory of your fasta files 
##The output will be files with all the DRS and IRS in .cvs files


#PARTE 1


import os
import re
from modulos import salida
from modulos import combinaciones
from modulos import resultados


pwdactual = os.getcwd()
path = pwdactual
lstFiles = []
lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if extension == ".fasta":
            lstFiles.append(nombreFichero + extension)
            #print (nombreFichero+extension)
print(lstFiles)#
    
print('LISTADO FINALIZADO')#
print("Existen %s archivos con extension FASTA en tu directorio actual " % (len(lstFiles)))#


for arch in lstFiles:
    nombre = arch
    print('El nombre de tu archivo es:> ', nombre)
    fasta = open(nombre, 'r')
    secuencia = fasta.read()
    secuencia = secuencia.split('\n')
    informacion_de_la_secuencia = secuencia[0]
    secuencia = secuencia[1:]
    secuencia2 = ''.join(secuencia)
    secuencia2 = secuencia2.upper()
    #print(secuencia2)
    longitud = len(secuencia2)
    print('el tamanio original de tu secuencia es de: ', longitud, 'pb')
    ##Esta parte de codigo elimina las Ns de la secuencia
    secuencia = []
    contador_de_N = []

    for base in secuencia2:
        if base != 'N':
            secuencia.append(base)
        if base == 'N':
            contador_de_N.append(base)

    contador_de_N = len(contador_de_N)
    print('Se eliminaron de tu secuencia:', contador_de_N, 'Ns')

    secuencia = ''.join(secuencia)
    #print(secuencia)
    longitud = len(secuencia)
    print('Este es el tamaño de tu secuencia sin Ns:>', longitud)
    print('Esta es la informacion de tu secuencia :> \n', informacion_de_la_secuencia)

    

#PARTE2
    combinaciones (5,secuencia,nombre)
    combinaciones (6,secuencia,nombre)
    combinaciones (7,secuencia,nombre)
    combinaciones (8,secuencia,nombre)
    combinaciones (9,secuencia,nombre)
    combinaciones (10,secuencia,nombre)
    combinaciones (11,secuencia,nombre)
    combinaciones (12,secuencia,nombre)
    combinaciones (13,secuencia,nombre)
    combinaciones (14,secuencia,nombre)
    combinaciones (15,secuencia,nombre)
    combinaciones (16,secuencia,nombre)
    combinaciones (17,secuencia,nombre)
    combinaciones (18,secuencia,nombre)
    combinaciones (19,secuencia,nombre)
    combinaciones (20,secuencia,nombre)
    combinaciones (21,secuencia,nombre)
    combinaciones (22,secuencia,nombre)
    combinaciones (23,secuencia,nombre)
    combinaciones (24,secuencia,nombre)
    combinaciones (25,secuencia,nombre)
    combinaciones (26,secuencia,nombre)
    combinaciones (27,secuencia,nombre)
    combinaciones (28,secuencia,nombre)
    combinaciones (29,secuencia,nombre)
    combinaciones (30,secuencia,nombre)
    


#PARTE 5

salida ()

#PARTE 6
resultados ()






            
















































