def patternCount(text, pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if text[i:len(pattern)+i]==pattern:
			count +=1
	return(count)

#print(patternCount('GATTACAT', 'AT'))

def nucCount(seq):
	mybases = {'A':0, 'T':0, 'C':0, 'G':0}
	for i in range(len(seq)):
		n = seq[i]
		mybases[n]+=1
	return mybases
print(nucCount('GATTACAT'))