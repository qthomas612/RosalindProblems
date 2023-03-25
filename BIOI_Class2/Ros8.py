#Ros8.py
#quinn thomas
#Rosalind 8

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba3e.txt", 'r').read().split()
#create output file
outfile = open(mydir + 'Ros8.txt', 'w')

sequences = infile[0:]

def idkyet(seqs):
	#initialize dictionary and output string
	bruijn = {}
	string = ""
	#for each sequence in the input file
	for item in seqs:
		#identify the prefix and suffix in the current sequence
		pre = item[0:len(item)-1]
		#print(pre)
		suff = item[1:len(item)+1]
		#print(suff)
		#check to see if prefix is already in dictionary
		if pre in bruijn:
			#if yes, append to current value
			bruijn[pre].append(suff)
		else:
			bruijn[pre] = [suff]
	#sort items in your adjacency list
	for key, value in sorted(bruijn.items()):
		#change any lists to strings
		string += key+ ' -> '+ ",".join(map(str,(value))) +'\n'
	return(string)
outfile.write(idkyet(sequences))
outfile.close()