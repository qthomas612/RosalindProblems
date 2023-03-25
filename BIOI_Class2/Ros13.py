'''
Ros13.py
quinn thomas
Rosalind 13
The Last-to-First array, denoted LastToFirst(i), 
answers the following question: given a symbol at position i 
in LastColumn, what is its position in FirstColumn?
most of this code was copied from problem 11
'''
import os

'''
Given: A string BWT(Text), followed by a collection of strings Patterns.
Return: A list of integers, where the i-th integer corresponds to the 
number of substring matches of the i-th member of Patterns in Text.
'''

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "Ros13Prac.txt", 'r').read().split()
#create output file
outfile = open(mydir + 'Ros13.txt', 'w')

seq = infile[0]
patterns = infile[1:]

#print(seq)
#print(patterns)
last_list = []
for i in seq:
	last_list.append(i)

first_list = sorted(last_list)

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
nList = ["$", "A", "C", "T", "G"]
# I did this formatting to make the for loops easier in the indexes function
firsts = [first_dolla, first_As, first_Cs, first_Ts, first_Gs]
lasts = [last_dolla, last_As, last_Cs, last_Ts, last_Gs]


# at this point we have two lists with our lexicographic nucleotides
# and our BWT
#this function basically indexes all the nucleotides in both lists

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
qlast_idxs = indexes(last_list, nList, lasts)
#print(first_idxs)

last_idxs = []
for item in qlast_idxs:
	last_idxs += item

#print(last_idxs)


def find_Pattern(firstCol, lastCol, lastSeq, pattern):
	top = int(0)
	bottom = int(len(firstCol))
	pat = pattern
	#print(type(top))
	#print(type(bottom))
	#print(lastCol)
	while top <= bottom:
		if len(pat) > 0:
			curr_nuc = pat[-1]
			print(curr_nuc)
			pat = pat[0:-1]
			#print(pattern)
			#if positions from top to bottom in LastColumn contain an occurrence of symbol
			curr_list = lastCol[top:bottom+1]
			#print(curr_list)
			if curr_nuc in curr_list:
				top_index = lastCol.index(curr_nuc)+top #first occurence of symbol in lastCol
				print(top_index)
				bottom_index = len(lastCol)-lastCol[::-1].index(curr_nuc)+top-1 #last pos of symbol in lastCol
				print(bottom_index)
				top = lastSeq(lastCol, top_index)
				print(top)
				bottom = lastSeq(lastCol, bottom_index)
				print(bottom)
			else:
				return 0

		else:
			return bottom-top+1



pattern_occurences = []
'''
for pattern in patterns:
	count = find_Pattern(first_list, last_list, last_idxs, pattern)
	pattern_occurences.append(count)
'''
print(first_list)
print(last_list)
print(last_idxs)
print(patterns[0])


test = find_Pattern(first_list, last_list, last_idxs, patterns[0])
print("This is test:", test)
#print(pattern_occurences)

#answer_as_list = tranform(first_list, last_list, first_idxs, last_idxs)
#print(answer_as_list)


'''
def tranform(fL, lL, fI, lI):
	#where we are going to add nucleotides for our final answer
	start_seq = ['$']
	#this is our starting point for the first list
	idx = 0
	#exit strategy for the while loop
	loop_len = len(fL)

	while loop_len > 1:
		#using the index from the lexicorgraphic list
		#find the corresponding nucelotide from last list
		letter = last_list[idx]
		#append letter to the beginning of the final list
		#start_seq.insert(0, letter)
		# search last_idx for idx location
		last_idx = find_idxs(lI, idx)
		#print(last_idx) #tester
		# find location of matching index value in firs_idx list
		# ps this works bc of the way we formatted our index lists
		first_idx= fI[last_idx[0]][last_idx[1]]
		#print(first_idx)
		#reassign this new index value as our current index
		idx = first_idx
		#exit strategy
		loop_len -=1
		#back to top of loop
	return(start_seq)


#in this function we are looking for the location of the value of
# our current index in our list of indexes from the last str
def find_idxs(lI, idx):
	#bc we have nested lists we need a for loop
    for nest_list in lI:
    	#if we find the matching index value
        if idx in nest_list:
        	#return the location of that index value
            return [lI.index(nest_list), nest_list.index(idx)]
    #basically our else statement if no matches are found so
    #the program doesn't freak out
    raise ValueError("'{idx}' is not in list".format(idx = idx))
'''

'''
our input is 4 lists:
two which have our first and last sequences
two which have our first and last indexes
'''








