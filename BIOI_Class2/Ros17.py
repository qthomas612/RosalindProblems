#Ros17.py
#quinn thomas
#Rosalind 17
import os
import math
#import numpy as np

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "Ros17Prac.txt", 'r').readlines()
#create output file
outfile = open(mydir + 'Ros17.txt', 'w')

n = int(infile[0])
distance_matrix = []
print(n)
#print(distance_matrix)

for line in infile[1:]:
	line = line.strip().split()
	#print(line)
	dim = []
	for item in line:
		item = float(item)
		if item == 0:
			item = float('inf')
		dim.append(item)
	distance_matrix.append(dim)

print(distance_matrix)

smallest_value = float('inf')

#min vals in each line
for value in distance_matrix:
	curr_value = min(value)
	if curr_value < smallest_value:
		smallest_value = curr_value
print(smallest_value)

#print(smallest_value)

'''
HierarchicalClustering(D, n):
	Clusters ← n single-element clusters labeled 1, ... , n
 	construct a graph T with n isolated nodes labeled by single elements 1, ... , n
	while there is more than one cluster 
		find the two closest clusters Ci and Cj  
		merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
		add a new node labeled by cluster Cnew to T
		connect node Cnew to Ci and Cj by directed edges 
		remove the rows and columns of D corresponding to Ci and Cj 
		remove Ci and Cj from Clusters 
		add a row/column to D for Cnew by computing D(Cnew, C) for each C in Clusters
		add Cnew to Clusters 
	assign root in T as a node with no incoming edges
	return T

'''
