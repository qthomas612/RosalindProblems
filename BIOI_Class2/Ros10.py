#Ros10.py
#quinn thomas
#Rosalind 10
import os

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "Ros10Prac.txt", 'r').read()
#create output file
outfile = open(mydir + 'Ros10.txt', 'w')


#print(infile[0:-1])

curr_str = ''
new_str = ''
arr= []
y=[]


def transform(my, arr, curr_str, count):
	#print(count)
	if count == 0:
		return sorted(my)
	else:
		new_str = curr_str[-1]+curr_str[0:len(curr_str)-1]
		my = arr.append(new_str)
		#print(curr_str)
		#print(new_str)
		print(arr)
		transform(my, arr, new_str, count-1)
	
	
def findBWT(my_arr):
	bwt = ""
	my_arr = my_arr.sort()
	for item in my_arr:
		btw+= item[-1]
	print(btw)



print(transform(y, arr, infile, len(infile)))