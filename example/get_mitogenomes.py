#!/usr/bin/env python
# -*- coding: utf-8

########################################
#get_mitogenomes.py                    #
#Program by Noel Cabañas               #
#Diciembre 2019                        #
#Nota: Check licence in SalmonellaIIB  #
#e-mail: ncabanas@iibiomedicas.unam.mx #
########################################

#In order to work correctly you need install BIOPYTHON and the following modules

import datetime
import os
from Bio import SeqIO
from Bio import Entrez


#This script download fasta sequences. It as well can convert genbank sequences to fasta

def introduction():
    '''This function prints the date the script was made'''
    date = datetime.datetime(2019, 12, 11)  # You can write a predetermined date or use the system's date
    print('This script was wrote by Noel Cabañas on ' + date.strftime("%c \n"))
    print('Python version employed > 3.7.4 ( Default, Aug 13 2019, 15:17:50)')
    print("\nSalmonella IIB is working in your analysis.")
    


#This part of the script download fasta files only with the NCBI IDs
#MAke sure to change the Email from time to time otherwise your connection is interrupted and only is able to download some sequences, be careful!!!


def fastaFiles(singleID):
	"""Downloading fasta files"""
	Entrez.email = "nnns@example.com" #e-mail
	handle = Entrez.efetch(db='nucleotide',id=singleID, rettype = 'fasta', retmode= 'text')
	f = open('%s.fasta' % singleID, 'w')
	f.write(handle.read())
	handle.close()
	f.close()

#fastaFiles('NC_001573.1') #You need to uncomment this line if you want to download a single fasta file, or multiple sequences manually.

#With this code you are downloading multiple fasta files. The NCBI IDs are read from a text file which make easier the work.
entries = open('ids.txt', 'r')
for entry in entries:
	entryy= entry.strip()
	print (entryy)
	fastaFiles(entryy)



##########This part of the script is automatized to generate the complete analysis with a click
os.rename('ids.txt','ids.ll')
os.makedirs('repeats/results/results_by_size')
os.makedirs('repeats/fasta_files')
os.system('mv *.fasta ./repeats')
os.system ('cp -n *repeats.py ./repeats')
os.system ('cp -n result_by_size.py ./repeats/results/results_by_size')
os.system ('cp -n ids.ll ./repeats/results/results_by_size')
os.rename('ids.ll','ids.txt')
os.chdir('./repeats')###If this line is uncommented you are running all the scripts autotically
os.system('python mito_repeats.py')###If this line is uncommented you are running all the scripts autotically
os.system('mv *.fasta ./fasta_files')
os.system('mv resultsSRD.txt.csv ./results/results_by_size')
os.system('mv resultsSRI.txt.csv ./results/results_by_size')
os.system('mv *.csv ./results')
os.remove('mito_repeats.py')
os.remove('repeats.py')
os.chdir('./results/results_by_size')
os.rename('ids.ll','ids.txt')
os.system('python result_by_size.py')
os.remove('ids.txt')
os.remove('result_by_size.py')


#########################################################################################	
###This code is not used in the analyses, but can be helpful for other analyses.
#This part of the script convert a genbak format to a fasta format 	
def convertFormat(sequence):
	"""convert a genbank file to a fasta format file"""
	for seq_record in SeqIO.parse(sequence, "genbank"):
		count = SeqIO.convert(sequence, "genbank", "%s.fasta" %seq_record.id, "fasta")
		print("Converted %i records" % count)

#convertFormat("_NC_001573.1.gbk") #write here the name of the gebank file that you want to convert to fasta
