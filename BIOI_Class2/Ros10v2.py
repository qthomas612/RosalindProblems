#Ros10.py
#quinn thomas
#Rosalind 10
import os

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba9i.txt", 'r').read().splitlines()
#create output file
outfile = open(mydir + 'Ros10.txt', 'w')

#print(infile)

curr_str = infile[0]
#print(curr_str)
new_str = ''
my_list = []
#for each nucleotide in our str
for i in curr_str:
	#shuffle the letters to create a new str
	new_str = curr_str[-1]+curr_str[0:len(curr_str)-1]
	#add the new string to our list
	my_list.append(new_str)
	#send it back to shuffle at the next index
	curr_str = new_str

#sort list lexicographically
my_list = sorted(my_list)
#print(my_list)

bwt = ""
#add the last letter of each item in the list to our empty str
for item in my_list:
	bwt+= item[-1]

#after each letter is added we have our transformation
print(bwt)
outfile.write(bwt)
outfile.close()