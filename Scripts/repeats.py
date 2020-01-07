#!/usr/bin/env python
# -*- coding: utf-8

########################################
#repeats.py                            #
#Programa creado por Noel Cabañas      #
#Febrero de 2016                       #
#Nota: para permisos y mayores detalles#
#comunicarse al correo                 #
#e-mail: noel-102@hotmail.com          #
########################################



########################################
#repeats.py                            #
#Scritp created by por Noel Cabañas    #
#Febrero de 2016                       #
#Note: It is an open-source, that can be#
#used under request.                    #
#e-mail: ncabanas@iibiomedicas.unam.mx  #
########################################



##This program is used by mito_repeats.py which is the original program to identify the repeat sequences in the mitogenomes


import re
def combinaciones (tamaño, secuencia,nombre):
    #PARTE2
    
#Combinaciones de 5
    tamanio_deseado= tamaño
    indice = 0
    longitud = len(secuencia)
    combinaciones = []
    ys=str(tamaño)

    while tamanio_deseado <= longitud:
        combinaciones.append(secuencia[indice:tamanio_deseado])
        indice = indice + 1
        tamanio_deseado = tamanio_deseado + 1

    combinaciones_sin_repetir = []

    for combinacion in combinaciones:
        if combinacion not in combinaciones_sin_repetir:
            combinaciones_sin_repetir.append(combinacion)

    #print(len (combinaciones_sin_repetir))


    
#PARTE 3

    for combinacion5 in combinaciones_sin_repetir:
        sek=secuencia
        need=combinacion5
        ind=[m.start() for m in re.finditer(r'{}'.format(re.escape(need)), sek)]
        ll2=[]
        for t in ind:
            y=t+1
            ll2.append (y)
            
        fin=len (ll2),combinacion5,ll2
        fin2=str (fin)
        fin3=len (ll2)
        if fin3 >=2:
            namecsv=nombre.split('.')
            f=open(namecsv[0]+'-SRD-'+ys+'-'+'.txt', 'a', encoding='utf-8')
            f.write (fin2 + '\n')
            f.close ()  
#PARTE 4


            
    #Este codigo crea la caedana complementaria y la invierte para poder buscar las SRI
    
    #print (secuencia) #secuencia original
    secuencia3=secuencia
    #print (secuencia2) 
    for nucle_otido in secuencia3:
        secuencia3=secuencia3.replace ('A', '1')
        secuencia3=secuencia3.replace ('T', '2')
        secuencia3=secuencia3.replace ('G', '3')
        secuencia3=secuencia3.replace ('C', '4')
    #print (secuencia2)
    for numer in secuencia3:
        secuencia3=secuencia3.replace ('1', 'T')
        secuencia3=secuencia3.replace ('2', 'A')
        secuencia3=secuencia3.replace ('3', 'C')
        secuencia3=secuencia3.replace ('4', 'G')
    #print (secuencia2) #secuencia complememtaria de 3' a 5'
    secuencia3=secuencia3 [::-1]
##    p=open ('seqinv', 'a')
##    p.write(secuencia2)
##    p.close
    print('ANALYZING '*4)


    for combinacion5 in combinaciones_sin_repetir:
        sek=secuencia3
        need=combinacion5
        ind=[m.start() for m in re.finditer(r'{}'.format(re.escape(need)), sek)]
        ll2=[]
        for t in ind:
            y=t+1
            ll2.append (y)
            
        fin=len (ll2),combinacion5,ll2
        fin2=str (fin)
        fin3=len (ll2)
        if fin3 >=2:
            namecsv=nombre.split('.')
            f=open(namecsv[0]+'-SRI-'+ys+'-'+'.txt', 'a', encoding='utf-8')
            f.write (fin2 + '\n')
            f.close ()



#PARTE 5
import os
def salida ():
    pwdactual2 = os.getcwd()
    path2 = pwdactual2
    lsFiles = []
    lsDir = os.walk(path2)  # os.walk()Lista directorios y ficheros
    for root, dirs, files in lsDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if extension == ".txt":
                lsFiles.append(nombreFichero + extension)
                #print (nombreFichero+extension)


    for arc in lsFiles:
        filename = arc
        char1 = '('
        char2 = ''
        char3 = ')'
        char4 = '['
        char5 = ']'
        char6 = " "
        char7 = "'"

        filer = open(filename, "r")
        filew = open(filename+'.csv', "w")
        buff = filer.read()
        rbuff = buff.replace(char1, char2)
        rbuff2 =rbuff.replace (char3,char2)
        rbuff3 =rbuff2.replace (char4,char2)
        rbuff4 =rbuff3.replace (char5,char2)
        rbuff5 = rbuff4.replace (char6,char2)
        rbuff6 = rbuff5.replace (char7,char2) 
        filew.write(rbuff4)
        filer.close()
        filew.close()
        os.remove (filename)



import os
import re

def resultados ():
    pwdactual = os.getcwd()
    path = pwdactual
    lstFiles = []
    lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if extension == ".csv":
                lstFiles.append(nombreFichero + extension)
                #print (nombreFichero+extension)
    #print(lstFiles)#
    #print('LISTADO FINALIZADO')#


    for arch in lstFiles:
        j1=arch
        jj=j1.split ('-')
        if jj[1] == 'SRD':
            tabla= open (j1, 'r')
            #print (arch)
            cc=0
            contador=0
            for linea in tabla:
                ll2=linea.split (',')
                ll3=ll2[0]
                contador+=1
                if ll3 != '': 
                    ll4=int(ll3)
                    #print (ll3)
                    cc=cc+ll4
                    #print(cc)
            tabla.close()
            f=open('resultsSRD.txt', 'a')
            #rr=arch,cc,contador  #nombre del archivo,suma de numero de secuencias repetidas totales,conatdor de numero de secuencias que estan repetidas
            rr=arch,cc
            rr=str (rr)
            f.write (rr+'\n')
            f.close ()
        if jj[1] == 'SRI':
            tabla= open (j1, 'r')
            #print (arch)
            cc=0
            contador=0
            for linea in tabla:
                ll2=linea.split (',')
                ll3=ll2[0]
                contador+=1
                if ll3 != '': 
                    ll4=int(ll3)
                    #print (ll3)
                    cc=cc+ll4
                    #print(cc)
            tabla.close()
            f=open('resultsSRI.txt', 'a')
            #rr=arch,cc,contador  #nombre del archivo,suma de numero de secuencias repetidas totales,conatdor de numero de secuencias que estan repetidas
            rr=arch,cc
            rr=str (rr)
            f.write (rr+'\n')
            f.close () 
            
        
    filename ='resultsSRD.txt'
    char1 = '('
    char2 = ''
    char3 = ')'
    char4 = '['
    char5 = ']'
    char6 = " "
    char7 = "'"

    filer = open(filename, "r")
    filew = open(filename+'.csv', "w")
    buff = filer.read()
    rbuff = buff.replace(char1, char2)
    rbuff2 =rbuff.replace (char3,char2)
    rbuff3 =rbuff2.replace (char4,char2)
    rbuff4 =rbuff3.replace (char5,char2)
    rbuff5 = rbuff4.replace (char6,char2)
    rbuff6 = rbuff5.replace (char7,char2) 
    filew.write(rbuff4)
    filer.close()
    filew.close()
    os.remove (filename)

    filename ='resultsSRI.txt'
    char1 = '('
    char2 = ''
    char3 = ')'
    char4 = '['
    char5 = ']'
    char6 = " "
    char7 = "'"

    filer = open(filename, "r")
    filew = open(filename+'.csv', "w")
    buff = filer.read()
    rbuff = buff.replace(char1, char2)
    rbuff2 =rbuff.replace (char3,char2)
    rbuff3 =rbuff2.replace (char4,char2)
    rbuff4 =rbuff3.replace (char5,char2)
    rbuff5 = rbuff4.replace (char6,char2)
    rbuff6 = rbuff5.replace (char7,char2) 
    filew.write(rbuff4)
    filer.close()
    filew.close()
    os.remove (filename)


