#Quinn Thomas
#Rosalind Problem4
#Citation: https://www.mrgraeme.com/greedy-motif-search/

import os
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
infile = open(mydir + "rosalind_ba2d.txt", 'r').read().splitlines()
outfile = open(mydir + 'Ros4out.txt', 'w')
numbers = infile[0].split()
#length of kmer
kmerLength = int(numbers[0])
#number of sequences
numSeqs = int(numbers[1])
#list of dna sequences
sequences = infile[1:len(infile)]
#print(sequences) #tester

#initialize the first motif list
def initializeMotif(k, t, dna):
	initMat = []
	for item in dna:
		initMat.append(item[0:k])
	return(initMat)

def greed(k, t, dna, initMotif):
	#save our first motif list as the best
	bestMotif = initMotif
	#iterate through first sequence
	for i in range(len(dna[0])-k+1):
		moList = []
		#start a list for each kmer in the first sequence
		moList.append(dna[0][i:i+k])
		#print(moList)	#tester
		for n  in range(1,t):
			#send kmer from first sequence to make a current profile using frequencies
			prof = getProf(moList)
			#send the profile, sequence you're working on
			#and the length of your kmer to 
			#print(prof) #tester
			moList.append(find_best_mer(prof, dna[n], k))
		#at this point we have two lists of mers and need to compare
		#the liklihood of each using hamming
		if scoreMatrix(bestMotif) > scoreMatrix(moList):
			bestMotif = moList
	return bestMotif


def getProf(moList):
	profile = []
	#print(moList)
	for i in range(len(moList[0])):
		#initialize nucleotide counts
		countA=0
		countC=0
		countG=0
		countT=0
		#count nucleotides at each location in mer
		for item in moList:
			if item[i] == 'A':
				countA += 1
			elif item[i] == 'C':
				countC += 1
			elif item[i] == 'G':
				countG += 1
			elif item[i] == 'T':
				countT += 1
		#calculate the frequency of each nucleotide in mer
		probA = countA/len(moList)
		probC = countC/len(moList)
		probG = countG/len(moList)
		probT = countT/len(moList)
		#add frequencies to a list to make profile
		profile.append([probA, probC, probG, probT])
	return profile

#here we are going to compare the profile to the sequence sent
#to determine which mer has the best match
def find_best_mer(prof, seq, k):
	#initialize best matching kmer
	bestMer = seq[0:0+k]
	bestProb = 0
	for i in range(len(seq)-k+1):
		#go through every kmer in sequence that was sent
		currmer = seq[i:i+k]
		prob = 1
		#determine the probability of the kmer by comparing it 
		#to the profile that was initialized
		for x in range(len(currmer)):
			if currmer[x] == 'A':
				#frequency of letters given by profile
				prob = prob*prof[x][0]
			elif currmer[x] == 'C':
				prob = prob*prof[x][1]
			elif currmer[x] == 'G':
				prob = prob*prof[x][2]
			elif currmer[x] == 'T':
				prob = prob*prof[x][3]
		if prob>bestProb:
			bestProb = prob
			bestMer = currmer
	return bestMer

def scoreMatrix(motifList):
	#initialize empty consensus sequence and hamming score
	con_seq = ""
	score = 0
	for i in range(len(motifList[0])):
		#initialize nucleotide counts
		countA=0
		countC=0
		countG=0
		countT=0
		#count nucleotides at each location in mer
		for item in motifList:
			if item[i] == 'A':
				countA += 1
			elif item[i] == 'C':
				countC += 1
			elif item[i] == 'G':
				countG += 1
			elif item[i] == 'T':
				countT += 1
		#now check what the most frequent nucleotide is at each location
		if countA >= max(countC, countG, countT):
			con_seq += "A"
		elif countC >= max(countA, countG, countT):
			con_seq += "C"
		elif countG >= max(countC, countA, countT):
			con_seq += "G"
		elif countT >= max(countC, countG, countA):
			con_seq += "T"
	#now that we have a consensus sequence we can compare
	#motifs to consensus by calculating hamming distance
	for motif in motifList:
		for x in range(len(motif)):
			if motif[x] != con_seq[x]:
				score += 1
	return score

init_List = initializeMotif(kmerLength, numSeqs, sequences)
merList = greed(kmerLength, numSeqs, sequences, init_List)
#change from list to str
finalMers = ""
for l in merList:
	finalMers += l + "\n"
outfile.write(finalMers)
outfile.close()
