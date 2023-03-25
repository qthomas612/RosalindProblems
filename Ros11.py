import os
#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_Ros/"
#save input file to variable #rstrip removes the new line character from the input file
myfile = open( mydir + "rosalind_orf.txt").read().split()
#create the output file
outfile = open(mydir + 'rosOut_11.txt', 'w')

#create DNA dictionary for reverse complement strand
DNA_dict = {
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'}

#create a variable for the forwards and reverse sequences
fseq = ''
for i in range(1, len(myfile)): #add everythings except the header to your forward sequence
    fseq += myfile[i]
#print(fseq)    #debug tester
rev_comp = ''
for i in fseq:
    #save the complements of this strand in reverse order to get the reverse complement
    rev_comp = DNA_dict[i] + rev_comp

#create a dictionary with the genetic code for DNA
gencode = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP', 
        'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W'}


#create a function that takes parameters for a counter and the sequence
def foundATG(i, sequence):
    AAseq = ''      #variable to hold amino acid sequence
    endoflist = len(sequence)-2
    for x in range(i,len(sequence)-2, 3):
        codon = sequence[x:x+3]   #asigns three letters to codon to search for it in our dictionary
        #print(codon)   #debug tester
        AAcid = gencode[codon]  #search for amino acid in dictionary
        if AAcid == "STOP": #if Amino acid is a stop codon
            return AAseq    #return the amino acid list to our main function
        elif x == endoflist:#if we reached the end of the list without a stop codon
            return null
        else:
            AAseq += AAcid  #add amino acid to amino acid sequence
    
#create a function that will search for ATG within a given sequence 
def findATG(seq):
    count = 0
    start = 'ATG'
    orf_list = []
    while count < len(seq)-2:   #iterates through the whole sequence to look for ATG
        codon = seq[count:count+3]  
        if codon == start:      #if ATG is found
            #print(count) #debug tester
            pseq = foundATG(count, seq)     #send location and sequence to foundATG function
            #print(pseq) #debug tester
            orf_list.append(pseq)           #when amino acid sequence is returned add it to the orf_list
        count+=1        #increase the count variable for every loop
    return(orf_list)         
        
orf = findATG(fseq) + findATG(rev_comp) #combine your orfs from your two complementary strands
orf = filter(None, orf)    #this removes all of the nones that were returned from foundATG
print(orf)
condensed_orf = list(dict.fromkeys(orf))  #remove repeats from your orf list
for j in condensed_orf:     #write out each item from your orf list to your output file
    outfile.write(j+'\n')
outfile.close()












            
