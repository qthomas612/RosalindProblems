import os
#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_Ros/"
#save input file to variable #split the file into the two sequences
infile = open( mydir + "rosalind_hamm.txt").read().split('\n')
#create the output file
outfile = open(mydir + 'rosOut_10.txt', 'w')

#print(infile)  #debug tester

#create variables for the two sequences
seq1 = infile[0]
seq2 = infile[1]
#create a counter variable to count mismatches
counter = 0

#create a for loop for the length of the sequences
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:  #if the characters are not the same add one to counter
        counter+=1

#print(counter) #debug tester
outfile.write(str(counter)) #write counter to output file
outfile.close() #close file
