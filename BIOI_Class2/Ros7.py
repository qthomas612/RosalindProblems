#Ros7.py
#quinn thomas
#Rosalind 7

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba3d.txt", 'r').read().split()
#create output file
outfile = open(mydir + 'Ros7.txt', 'w')

length = int(infile[0])
sequence = infile[1]

def idkyet(k, seq):
	#initialize dictionary and output string
	bruijn = {}
	string = ""
	for i in range(len(seq)-k+1):
		kmer = seq[i:i+k]
		#identify prefix and suffix
		prefix = kmer[0:k-1]
		suffix = kmer[1:k+1]
		#check to see if the prefix already exists in dictionary
		if prefix in bruijn:
			#if yes, append to current value
			bruijn[prefix].append(suffix)
		else:
			bruijn[prefix] = [suffix]
	#sort items in your adjacency list
	for key, value in sorted(bruijn.items()):
		#change any lists to strings
		string += key+ ' -> '+ ",".join(map(str,(value))) +'\n'
	return(string)
	
#write string to your output file
outfile.write(idkyet(length, sequence))
outfile.close()
