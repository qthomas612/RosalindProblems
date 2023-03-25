#Ros11.py
#quinn thomas
#Rosalind 11
import os

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read 
infile = open(mydir + "rosalind_ba9j.txt", 'r').read()
#create output file
outfile = open(mydir + 'Ros11.txt', 'w')

last_list = []
for i in infile:
	last_list.append(i)

first_list = sorted(last_list)
#print(first_list)
#print(last_list)


#easier for me to visualize
#first
#['$', 'A', 'A', 'A', 'C', 'C', 'C', 'G', 'T', 'T', 'T']
#last
#['T', 'T', 'C', 'C', 'T', 'A', 'A', 'C', 'G', '$', 'A']

#I think I made this way more complicated than it needed to be
#these are all the variables I want to keep track of
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
last_idxs = indexes(last_list, nList, lasts)
#print(last_idxs)


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
		start_seq.insert(0, letter)
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

#our input is 4 lists:
#two which have our first and last sequences
#two which have our first and last indexes
answer_as_list = tranform(first_list, last_list, first_idxs, last_idxs)

#print(len(last_list))

#changing formatting from list to str
answer = ''
for value in answer_as_list:
	answer += value

print(answer)

outfile.write(answer)
outfile.close()



