from Bio import Entrez
#from Bio import SeqIO
Entrez.email = "qthomas@luc.edu"    #tell NCBI who I am

mydir = "/Users/QuinnThomas/Desktop/BIOI_488/BIOI_Ros/"
infile = open(mydir + "rosalind_gbk.txt").read().split()   #separate the items in input file
outfile = open(mydir + 'rosOut_14.txt', 'w')
#print(infile) #debug tester

#search the NCBI database for the genus name and sort it to show only entries published
#between the dates given from the input file
handle = Entrez.esearch(db="nucleotide", term = infile[0]+'[Organism]',
        datetype = "pdat", mindate = infile[1], maxdate = infile[2])

record = Entrez.read(handle)
#save the amount of entries to count variable
count = int(record["Count"])
print(count)
outfile.write(str(count))
outfile.close()
