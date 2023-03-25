import os
#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_Ros/"
#save input file to variable #rstrip removes the new line character from the input file
infile = open( mydir + "rosalind_revc.txt").read().rstrip()
#create the output file
outfile = open(mydir + 'rosOut_8.txt', 'w')

#print(infile) #debug tester

#create a dictionary with the DNA complements
DNA_dict = {
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'}

rev_comp = ""

#create a for loop that goes through to iterate through each letter of the DNA strand
for i in infile:
    #save the complements of this strand in reverse order to get the reverse complement
    rev_comp = DNA_dict[i] + rev_comp 
#write the reverse complement strand to the output file
outfile.write(rev_comp)
outfile.close()



