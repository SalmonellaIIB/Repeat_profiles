
# This script extract the total number of repeat sequences by size
#It creastes files were you can see the total of repeat sequences of a determined size


#it needs the files created for the scritp mito_repeats.py and the file ids.txt 


def resultbySize ():
    for size in range (5, 31):
        size=str(size)

        e=open ('ids.txt', 'r')
        l=e.read ()
        l1=l.split('\n')
        print (l1)


        f=open ('resultsSRD.txt.csv', 'r')

        SR=[]
        for x in f:
            #g=f.readline()
            d=x.split('-')
            d2=int (d[2])
            #print(d2)
            d1=d[1]
            
            if d1== 'SRD' and d[2] == size:
                u=open('resultsSRD%s.csv' %size, 'a')
                u.write (x)
                u.close()
                print(x)
        f.close()


        f=open ('resultsSRI.txt.csv', 'r')

        SR=[]
        for x in f:
            #g=f.readline()
            d=x.split('-')
            d2=int (d[2])
            #print(d2)
            d1=d[1]
            
            if d1== 'SRI' and d[2] == size:
                u=open('resultsSRI%s.csv' %size, 'a')
                u.write (x)
                u.close()
                print(x)

        f.close()

resultbySize()
