import os
#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_Ros/"
#save input file to variable #rstrip removes the new line character from the input file
infile = open( mydir + "rosalind_prot.txt").read().rstrip()
#create the output file
outfile = open(mydir + 'rosOut_9.txt', 'w')

#create an amino acid dictionary
gencode = {
    "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
    "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
    "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
    "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
    "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
    "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
    "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
    "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
    "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
    "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
    "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
    "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
    "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
    "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
    "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
    "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"}

#print(infile[0:0+3]) #debug tester

AAseq = ''      #create AAseq variable

#for loop that goes through entire input file for every third letter
for i in range(0,len(infile), 3):
    codon = infile[i:i+3]   #asigns three letters to codon so we can search for it in our dictionary
    #print(codon)   #debug tester
    AAcid = gencode[codon]  #search for amino acid in dictionary
    if AAcid == "STOP": #if Amino acid is a stop codon
        break           #then escape the for loop and end
    else:
        AAseq += AAcid  #Else add the amino acid to the sequence
#print(AAseq)   #debug tester
outfile.write(AAseq)    #write complete amino acid sequence to output file
outfile.close()
