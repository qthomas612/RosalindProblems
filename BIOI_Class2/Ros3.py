#Quinn Thomas
#Rosalind Problem3

import os
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
infile = open(mydir + "rosalind_ba2a.txt", 'r').read().splitlines()
outfile = open(mydir + 'Ros3out.txt', 'w')

#length of kmer
kmer = int(infile[0][0])
#highest number of mismatches
mismatch = int(infile[0][2])
#list of dna sequences
sequences = infile[1:len(infile)]
print(sequences) #tester


def generatekmer(klength):
	#list of bases
	nucleotides = ["A", "T", "G", "C"]
	klist = []
	#check kmer length before iterating
	#number is one bc we already start with single nucleotides in nucleotide variable
	if klength == 1:
		return nucleotides

	#recursive call to generate kmer function
	#math: 4^k where 4 is for every nucleotide that can be used
	#and k is for the length of the kmer
	else:
		#calls the function the length of kmer times
		for i in generatekmer(klength-1):
			#iterates through every possible nucleotide base
			for n in nucleotides:
				klist.append(i+n)
		return klist

kmerList = (generatekmer(kmer))

#tester
#print(4**kmer)
#print(len(kmerList))

def kdMotif(k, seqs, m):
	kdMotifs =[]
	for item in k:
		#send every kmer to see if it exists in all sequences
		#add whatever is returned to motif list
		kdMotifs.append(calcmatches(item, seqs, m))
	return kdMotifs


#mer score is what keeps track of how many sequences have 
#hamming distances that qualify
#minHam is the hamming distance with the least amount of mismatches
#hamScore is the hamming distance for each generated kmer
def calcmatches(mer, seqlist, maxmis):
	merScore = 0
	#for every sequence given
	for x in seqlist:
		#initialize minHam as the highest it could be
		minHam = len(mer)
		#in the range of sequence length minus kmer length
		for p in range(len(x)-len(mer)+1):
			#initialize hamming score
			hamScore = 0
			#for each observed kmer calculate a new hamming score
			for i in range(len(mer)):
				if x[p+i] != mer[i]:
					hamScore += 1
			#print(hamScore) #tester
			#check to see if new hamming score is less than the min score
			if hamScore < minHam:
				minHam = hamScore
		#check to see if sequence qualifies according to maxmismatches
		if minHam <=maxmis:
			merScore +=1
	#print(merScore) #tester
	if merScore ==len(seqlist):
		return mer


allVals = kdMotif(kmerList, sequences, mismatch)
finalList = list(filter(None, allVals))
print(finalList)
myList = ""
for l in finalList:
	myList += l + " "
outfile.write(myList)
outfile.close()

