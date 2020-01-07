#!/usr/bin/env python
# -*- coding: utf-8

#########################################
#random_seq.py                          #
#Scritp created by por Noel Cabañas     #
#April de 2015                          #
#Note: It is an open-source, that can be#
#used under request.                    #
#e-mail: ncabanas@iibiomedicas.unam.mx  #
#########################################

#ESte programa ingresa una secuencia fasta original y lo convierte en una secuencia ramdom por 10 veces
#This program randomized a nucleotide sequence 10 times


import os
import re
import random 


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


    seq=secuencia

  
    #seq = "TGCTTTAGTTGATGAGGGGGTGATAGGTGGATGGACGATGATGGGGGGGATAGACAGATGACGATGATGACGATGACGATGACGATAG"
    ram1="".join(random.sample(seq, len(seq)))

    print (seq)
    #print (ram1)
    print ('\n')

    ram2= "".join(random.sample(ram1, len(ram1)))
    #print (ram2)


    ram3= "".join(random.sample(ram2, len(ram2)))
    #print (ram3)

    ram4= "".join(random.sample(ram3, len(ram3)))
    #print (ram4)


    ram5= "".join(random.sample(ram4, len(ram4)))
    #print (ram5)

    ram6= "".join(random.sample(ram5, len(ram5)))
    #print (ram6)


    ram7= "".join(random.sample(ram6, len(ram6)))
    #print (ram7)

    ram8= "".join(random.sample(ram7, len(ram7)))
    #print (ram8)


    ram9= "".join(random.sample(ram8, len(ram8)))
    #sprint (ram9)

    ram10= "".join(random.sample(ram9, len(ram9)))
    print (ram10)


    f= open ('seqs_ramdom.fasta', 'a')
    f.write(informacion_de_la_secuencia +'\n' +ram10+ '\n'+'\n')
    f.close()




#seq = "TGCTTTAGTTGATGAGGGGGTGATAGGTGGATGGACGATGATGGGGGGGATAGACAGATGACGATGATGACGATGACGATGACGATAG"
#print ("".join(random.sample(seq, len(seq))))
