'''
Ros13.py
quinn thomas
Rosalind 13

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
infile = open(mydir + "rosalind_ba9l.txt", 'r').read().split()
#create output file
outfile = open(mydir + 'Ros13.txt', 'w')

lastCol = infile[0]
patterns = infile[1:]

firstCol = sorted(lastCol)
firstColr = firstCol
#print(firstCol)

last_map = []

#for every nucleotide in our transform, tell us where that nucleotide exists 
#in the lexicographic list and append to last_map list (sorted by our transform column)
for n in lastCol:
	index = firstColr.index(n)
	last_map.append(index)
	#by doing this we eliminate recognition of the same indeces
	firstColr[index] = None


#print(last_map)

def find_Pattern(firstCol, lastCol, last_map, pattern):
	top = int(0)
	bottom = len(firstCol)-1
	#print(type(top))
	#print(type(bottom))
	#print(lastCol)
	while top <= bottom:
		if pattern:
			curr_nuc = pattern[-1]
			#print(curr_nuc)
			pattern = pattern[0:-1]
			#print(pattern)
			#if positions from top to bottom in LastColumn contain an occurrence of symbol
			curr_list = lastCol[top:bottom+1]
			#print(curr_list)
			#print(curr_list)
			if curr_nuc in curr_list:
				'''
				First occurence of symbol in our abbr list (curr_list) from lastCol.
				Since the list has been cut we have to update the indexes by 
				adding our previous top indeces.
				'''
				top_index = curr_list.index(curr_nuc)+top 
				#print(top_index)
				#last occurence of symbol in our abbr list from lastCol
				bottom_index = len(curr_list)-curr_list[::-1].index(curr_nuc)+top-1 
				#print(bottom_index)
				#find new top index using our list of mapped indexes
				top = last_map[top_index]
				#print(top)
				#find new bottom index using our list of mapped indexes
				bottom = last_map[bottom_index]
				#print(bottom)
			#if there are no matches, return 0
			else:
				return 0
		#otherwise return how many matches there are
		else:
			return bottom-top+1

#pattern = patterns[0]
#test = find_Pattern(firstCol, lastCol, my_index, pattern)
#print("This is test result:", test)

pattern_occurences = []

for pattern in patterns:
	#send all patterns to our find_pattern function
	count = find_Pattern(firstCol, lastCol, last_map, pattern)
	pattern_occurences.append(count)

answer = ''
for value in pattern_occurences:
	answer += str(value) + " "

print(answer)
outfile.write(answer)
outfile.close()

