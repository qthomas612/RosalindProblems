from Bio import SeqIO   #allows us to parse the data we retrieve
from Bio import Entrez  #allows us to access data from GenBank
mydir = "/Users/QuinnThomas/Desktop/BIOI_488/BIOI_Ros/"
infile = open(mydir + "rosalind_frmt.txt").read().split()
outfile = open(mydir + 'rosOut_13.txt', 'w')

Entrez.email = 'qthomas@luc.edu'    #let ncbi know who is accessing
#print(infile)

#collect the data from genbank by:
    #specifying the database we are looking through
    #entering the IDs from our input file
    #collect the data and set in fasta format
handle = Entrez.efetch(db = 'nucleotide', id = infile, rettype="fasta")
#parse the wrapper for the text and read it out to a list
records = list(SeqIO.parse(handle, 'fasta'))

#set the min length to something that will be replaced a smaller length later
min_length = 10000000000
#iterate through the fasta list
for item in records:
    #add the item description and sequence to string in fasta format
    mystr = '>'
    mystr += item.description + '\n'
    mystr += item.seq
    #calculate the length of the string we created
    curr_length = len(mystr)
    #if the length of str in less than the min length then
    #reassign min length and save the current item to variable
    if curr_length < min_length:
        min_length = curr_length
        min_item = mystr
    #print(mystr)

#print(min_item)
outfile.write(str(min_item))
outfile.close()
