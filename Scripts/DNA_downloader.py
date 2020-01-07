
#Program by Noel Cabañas               #
#Diciembre 2019                        #
#Nota: Check licence in SalmonellaIIB  #
#e-mail: ncabanas@iibiomedicas.unam.mx #
########################################

#########################################################################################	

#Download fasta files
#Put in a list named "ids.txt" the ncbi acces of the files you want to download

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

#########################################################################################	
#Download genbank Files and convert genbak files to fasta files

###This code is not used in the analyses, but can be helpful for other analyses.
#This part of the script convert a genbak format to a fasta format 	
def convertFormat(sequence):
	"""convert a genbank file to a fasta format file"""
	for seq_record in SeqIO.parse(sequence, "genbank"):
		count = SeqIO.convert(sequence, "genbank", "%s.fasta" %seq_record.id, "fasta")
		print("Converted %i records" % count)

#convertFormat("_NC_001573.1.gbk") #write here the name of the gebank file that you want to convert to fasta