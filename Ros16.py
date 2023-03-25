#from Bio import Entrez
#from Bio import SeqIO
from Bio.Seq import Seq

#Entrez.email = "qthomas@luc.edu"    #tell NCBI who I am

mydir = "/Users/QuinnThomas/Desktop/BIOI_488/BIOI_Ros/"
infile = open(mydir + "rosalind_orfr.txt").read().rstrip()
outfile = open(mydir + 'rosOut_16.txt', 'w')

#save the forward and reverse sequences to two variables
fseq = Seq(infile)
rseq = fseq.reverse_complement()

def translate(myseq, location):
    seq = myseq[location::]
    #biopython gives a warning if your sequence is not divisible by 3
    #to bypass just make exceptions by altering your sequence to make it
    #divisible by 3
    #then you can translate your sequence
    if len(seq) %3 == 0:
        orf = seq.translate()
        return orf
    elif len(seq) %3 == 1:
        orf = seq[:-1].translate()
        return orf
    elif len(seq) %3 == 2:
        orf = seq[:-2].translate()
        return orf

def find_orf(seq):
    protein_list = []
    for i in range(len(seq)):
        #search for start codon so we can translate the sequence
        codon = seq[i:i+3]
        if codon == 'ATG':
            proseq = translate(seq, i)
            #print(proseq)
            #append returned protein sequence to list
            protein_list.append(proseq)
    return protein_list

#create a list with all of your protein sequences
full_list = find_orf(fseq) + find_orf(rseq) 
max_length = 0      #make empty variable for length of the longest protein
for item in full_list:
    #because translate doesn't automatically stop at stop codons we need
    #to find them ourselves using .find
    protein_length = item.find("*")  
    #print(stop) #debug tester
    #find which of your sequences is the longest in nucleotides
    if protein_length > max_length:
        max_length = protein_length
        long_protein = item[0:protein_length]
#write your answer to output file
outfile.write(str(long_protein))
outfile.close()
    


