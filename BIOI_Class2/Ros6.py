#Ros6.py
#quinn thomas
#Rosalind 6

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba3c.txt", 'r').read().split()
#create output file
outfile = open(mydir + 'Ros6.txt', 'w')
#inf = None 


#create anempty dictionary
adjDict={}
#go through each item in list of sequences
for firstItem in infile:
	#assign a prefix
	prefix = firstItem[0:len(firstItem)-1]
	#for every prefix search for a suffix match in same sequence list
	for secondItem in infile:
		suffix = secondItem[1:len(secondItem)]
		#if prefix = suffix add the pair to dictionary
		if prefix == suffix:
			adjDict[firstItem] = secondItem
string = ""
for key, value in adjDict.items():
    string += key+ ' -> '+ value +'\n'
outfile.write(string)
outfile.close()












'''
def adjacency(seqs):
	adList = []
	for item in seqs:
		prefix = item[0:len(item)-1]
		newList = checkItems(prefix, item, seqs)
		adList+=newList
	return(adList)


def checkItems(prefix, currSeq, seqs):
	myList=[]
	for item in seqs:
		suffix = item[1:len(item)]
		if prefix == suffix:
			myList.append([item, currSeq])
	#print(myList)
	return myList

List = adjacency(infile)

def formatting(fList):
	for item in fList:
		string = item[0]+ " -> "+ item[1]
		print(string)
		#outfile.write(string)

formatting(List)
'''

'''
key : [5]
dict[key] = [5]
dict[key].append(6)
'''
