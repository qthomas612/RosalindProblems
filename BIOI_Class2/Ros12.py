#Ros12.py
#quinn thomas
#Rosalind 12
#The Last-to-First array, denoted LastToFirst(i), 
#answers the following question: given a symbol at position i 
#in LastColumn, what is its position in FirstColumn?
#most of this code was copied from problem 11
import os

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba9k.txt", 'r').read().splitlines()
#create output file
outfile = open(mydir + 'Ros12.txt', 'w')

seq = infile[0]
#position in last colomn
idx = int(infile[1])

#print(seq)
#print(idx)

#convert string to list
last_list = []
for i in seq:
	last_list.append(i)

first_list = sorted(last_list)

#print(first_list)
#print(last_list)

#initialize nested lists
first_As=[]
first_Cs=[]
first_Ts=[] 
first_Gs=[]
first_dolla =[]
last_As = []
last_Cs = []
last_Ts = []
last_Gs = []
last_dolla = []
nList = ["A", "C", "T", "G", "$"]
# I did this formatting to make the for loops easier in the indexes function
firsts = [first_As, first_Cs, first_Ts, first_Gs, first_dolla]
lasts = [last_As, last_Cs, last_Ts, last_Gs, last_dolla]



#this function indexes all the nucleotides in both forst 
#and last lists

def indexes(firstOrLast, nList, alist):
	c=0
	#for each nested list
	for item in alist:
		#identify which nucelotide list we are on
		nuc = nList[c]
		for i in range(len(firstOrLast)):
			#check to see if nucleotide is in sequence and 
			#if yes add index to nested list
			if firstOrLast[i] == nuc:
				item.append(i)
		#move on the next nucleotide
		c+=1
	return(alist)

first_idxs = indexes(first_list, nList, firsts)
last_idxs = indexes(last_list, nList, lasts)
#print(first_idxs)
#print(last_idxs)

def finder(fL, lL, fI, lI, idx):
	#sens list of indexes and index we are searching for and
	#returns the location of the match
	location_L = find_idxs(lI, idx)
	#find that same location in our first list and save the value
	first_idx = fI[location_L[0]][location_L[1]]
	return first_idx


def find_idxs(lI, idx):
	#bc we have nested lists we need a for loop
	for nest_list in lI:
		#print(nest_list)
		#if we find the matching index value
		if idx in nest_list:
			#return the location of that index value
			return [lI.index(nest_list), nest_list.index(idx)]
	#basically our else statement if no matches are found so
	#the program doesn't freak out
	raise ValueError("'{idx}' is not in list".format(idx = idx))

#our input is 4 lists:
#two which have our first and last sequences
#two which have our first and last indexes
answer = str(finder(first_list, last_list, first_idxs, last_idxs, idx))
print(answer)

outfile.write(answer)
outfile.close()



