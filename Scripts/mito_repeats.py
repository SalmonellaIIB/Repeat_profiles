#!/usr/bin/env python
# -*- coding: utf-8

########################################
#mito_repeats.py                            #
#Programa creado por Noel Cabañas      #
#Febrero de 2016                       #
#Nota: para permisos y mayores detalles#
#comunicarse al correo                 #
#e-mail: noel-102@hotmail.com          #
########################################


#######################################
#mito_repeats.py                                #
#Script created by Noel Cabañas        #
#Febrero de 2016                       #
#Note: It is an open-source, that can be#
#used under request.                    #
#e-mail: ncabanas@iibiomedicas.unam.mx  #
########################################

##This is the main scritp to identify the repeat sequences  in the mitogenomes
##You need repeats.py in order to run this script correctly
##You just need to run the program in the same directory of your fasta files 
##The output will be files with all the DRS and IRS in .cvs files


#PARTE 1

##Make sure that you have repeats.py and mito_repeats.pyin the same directory.They depend on each other.

import os
import re
from repeats import salida
from repeats import combinaciones
from repeats import resultados


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
    
#print('LISTADO FINALIZADO')#
print("There are %s files with FASTA extention in your current directory" % (len(lstFiles)))#


for arch in lstFiles:
    nombre = arch
    print('Name of the file analizing :> ', nombre)
    fasta = open(nombre, 'r')
    secuencia = fasta.read()
    secuencia = secuencia.split('\n')
    informacion_de_la_secuencia = secuencia[0]
    secuencia = secuencia[1:]
    secuencia2 = ''.join(secuencia)
    secuencia2 = secuencia2.upper()
    #print(secuencia2)
    longitud = len(secuencia2)
    print('The size of the sequence is : ', longitud, 'bp')
    ##This part of the code eliminate all the Ns in your sequence or unknown nucleotides
    secuencia = []
    contador_de_N = []

    for base in secuencia2:
        if base != 'N':
            secuencia.append(base)
        if base == 'N':
            contador_de_N.append(base)

    contador_de_N = len(contador_de_N)
    print('From your sequence were eliminated:', contador_de_N, 'Ns')

    secuencia = ''.join(secuencia)
    #print(secuencia)
    longitud = len(secuencia)
    print('This is the size of your sequence without Ns:>', longitud)
    print('This is the information of your sequence :> \n', informacion_de_la_secuencia)

    

#PART2
    for size in range (5, 31):
        combinaciones (size, secuencia,nombre)

    


#PART 5

salida ()

#PART 6
resultados ()

