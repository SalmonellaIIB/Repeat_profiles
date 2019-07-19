#Copyright <2016> Noel Cabañas
#Licensed under the Apache License, version 2.0. See LICENSE for details.


#!/usr/bin/env python
# -*- coding: utf-8


########################################
#divide_multifasta.py                  #
#Scritp created by Noel Cabañas        #
#Febrero de 2016                       #
#Note: It is an open-source, that can be#
#used under LICENSE.                    #
#e-mail: ncabanas@iibiomedicas.unam.mx  #
########################################


##Este programa ya se probo y funciona correctamente, es la version final que se debe utilizar
##This program runs correctly


##Needs python 3 or superior.
##This program split multifasta fles one by one and change the name of every file for the access ID number.
##Note:Do not modify the multifasta file before divide it, it must be the original file downloaded from the NCBI. Otherwise, the program would not be able to process your file.

##Este programa divide un archivo multifasta de uno en uno y les pone como nombre el numero de acceso
##NOTA: no se debe modificar el archivo multifasta antes de dividirlo, debe ser exactamente tal cual como se bajo del NCBI, de lo contrario el programa no funcionara correctamente


archivo = input('Ingresa el nombre de tu archivo multifasta, que quieres dividir:>')
multifasta = open(archivo, 'r')
multifasta1 = multifasta.read()
multifasta2 = multifasta1.split('\n\n')

# print (multifasta2)
noseq = len(multifasta2)
noseq2=noseq-1
print('Existen', noseq2, 'secuencias fasta en tu archivo multifasta', archivo, '\n')
print('Estos son los nombres de tus nuevos archivos fasta:')

try:
    for x in multifasta2:
        nom = x[1:30]
        nombre = nom.split('|')
        noacceso = nombre[3]
        print(noacceso)
        #print(x)
        f = open(noacceso + '.fasta', 'w')
        f.write(x)
        f.close()
except IndexError:
    print('Tu archivo multifasta se ha dividido correctamente')


    
    
    





