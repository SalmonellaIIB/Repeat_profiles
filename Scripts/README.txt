#These files were created by Noel Cabañas in order to perform analyses of repeat sequences in amphibians. 
#All of them are open sources, only make sure to cite the article>


#I list the files in this repository and small description.
#If you have problem do not hesitate to contact at: ncabanas@iibiomedicas.unam.mx



ids.txt----->This file contains the NCBI number access to download the mitogenomes. It need to be in the same folder with get_mitogenomes.py, mito_repeats.py and repeats.py.

get_mitogenomes.py-------> This scrip is the automatized version. It runs download the mitogenomes and runs the repeat sequences analysis. 

mito_repeats.py ----->This is the main Script that identify the DRS and IRS and generate .cvs files 

repeats.py----->This Script is used by the mito_repeats.py.py script, both need to be in the same directory, otherwise you won't  be able to run the scripts correctly.

ramdom_seq.py----->This script can randomized a sequence of nucleotides ten times.

result_by_size.py----->create tables where you can find the number of repeat and direct repeat sequences of different sizes for every mitogenome. 
