from Bio import SeqIO
mydir = "/Users/QuinnThomas/Desktop/BIOI_488/BIOI_Ros/"
infile = mydir + "rosalind_rvco.txt"
outfile = open(mydir + 'rosOut_12.txt', 'w')

#use parse function from the SeqIO module to parse fasta format file
#put each record into a list
records = list(SeqIO.parse(infile, 'fasta'))
count = 0   #initialize counter variable

for record in records:
    dna = record.seq    #store our sequence data in from record in dna variable
    #use reverse complement funciton on dna and store in rc_dna variable
    rc_dna = dna.reverse_complement()   
    if dna == rc_dna:   #if reverse comp is equal to the forward strand
        count+=1        #add to counter
        
print(count)
outfile.write(str(count))
outfile.close()
