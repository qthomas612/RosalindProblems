import os
#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba1d.txt", 'r')
a = (infile.read().splitlines())
patt = a[0]
text = a[1]
#create output file
outfile = open(mydir + 'Ros2out.txt', 'w')

def startPos(pattern, seq):
	positions = ""
	#iterate thorugh sequence
	for i in range(len(seq)-len(pattern)+1):
		#check to see if current index equals pattern
		if seq[i:i+len(pattern)] == pattern:
			#if yes, add index to positions
			positions+= str(i) +" "
	return(positions)

outfile.write((startPos(patt, text)))
outfile.close()