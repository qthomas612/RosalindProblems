#Ros5.py
#quinn thomas
#rosalind 5

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba3a.txt", 'r').read().split()
#create output file
outfile = open(mydir + 'Ros5.txt', 'w')

kmerLength = int(infile[0])
sequence = infile[1]
#print(kmerLength)
#print(sequence)

def kmerList(klength, seq):
	#create empty list
	klist = []
	#for each nucleotide in the sequence that generates a full kmer
	for i in range(len(seq)-klength+1):
		kmer = seq[i:i+klength]
		#add kmer to list
		klist.append(kmer)
	klist.sort()
	#print(klist)
	return klist


#change from list to str format
myList = '\n'.join(map(str, kmerList(kmerLength, sequence)))
#print(myList)
outfile.write(myList)
outfile.close()

