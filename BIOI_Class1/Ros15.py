import urllib.parse
import urllib.request
import re
from Bio import SeqIO

mydir = "/Users/QuinnThomas/Desktop/BIOI_488/BIOI_Ros/"
id_list = open(mydir + "rosalind_mprt.txt").read().split()
#because we are adding multiple lines at different points we need to append
outfile = open(mydir + 'rosOut_15.txt', 'a')

#for every id from the input file
j=0
for item in id_list:
    url = 'http://www.uniprot.org/uniprot/'+item+'.fasta'
    #open the webpage to retrieve fasta data
    data = urllib.request.urlopen(url)
    #this was something i found online that you need to do when fetching from
    #uniprot. it has to do with formating and encoding so this line of code
    #makes sure that we read the proper data to our variable
    #utf-8 is the format we want and we will ignore errors occurred
    fasta = data.read().decode('utf-8', 'ignore')
    #print(fasta)
    seq_start = fasta.find('\n')
    seq = fasta[seq_start+1:].replace("\n", "")
    seq = ' '+str(seq)
    #print(seq)
    #allows us to use this same pattern on multiple strs AKA a pattern object
    #compatible with our finditer later on
    #'r means raw str notation
    #?= is the lookahead regex for regular expressions
    N_motif = re.compile(r'N(?=[^P][ST][^P])')
    positions = []
    for x in range (len(seq)):
        #if the motif isn't found leave the loop
        if re.search(N_motif,seq[x+1:]) == None:
            break
        #if the motif is found add the position to our position list
        if re.match(N_motif,seq[x+1:]) != None:
            positions.append(x+1)
    if len(positions) > 0:
        outfile.write(id_list[j] + '\n')
        #this command tells us that we are going to join elements from the list
        #into a string and separate them by a space
        outfile.write(' '.join(map(str, positions)) + '\n')
    j+=1
outfile.close()


