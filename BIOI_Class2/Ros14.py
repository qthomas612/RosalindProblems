#Ros14.py
#quinn thomas
#Rosalind 14
import os
import math

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba8a.txt", 'r').readlines()
#create output file
outfile = open(mydir + 'Ros14.txt', 'w')


k = int(infile[0][0])
dim = int(infile[0][2])

data =[]
#This is all formatting the input
for line in infile[1:]:
	line =line.strip().split(" ")
	emptyList = []
	for num in line:
		num = float(num)
		emptyList.append(num)
	data.append(emptyList)

#print(data)

Centers = [data[0]]

#print(math.sqrt(9))
'''
NOTE TO SELF!
First thing you need to do is identify the closest center for all data points.
After each point is assigned a center measure distances between 
points and corresponding center.
Then find the maximum distance between points and their centers.
Last add the datapoint with the max distance to list of centers
'''

#where m is the dimensions, dp is the datapoint and cp is the center
def distance(m, cp, dp):
	sum = 0
	for i in range(m):
		sum+=(dp[i]-cp[i])**2
	#print(sum)
	dist = math.sqrt(sum)
	return dist

#distance(dim, [3.0, 3.0], [1.0, 0.0])


#Hopefully this function takes our list of center
def closestCenter(data, Centers):
	#while the list of centers does not equal to k
	while len(Centers) < k:
		#establish empty list for distances
		distList = []
		# for each data point
		for i in data:
			#intitialize a very high min distance
			minDist = float('inf')
			#for each center point
			for j in Centers:	
				# find the distance between the datapoint and center point
				currDist = distance(dim, j, i)
				#if our distance is less than the minimum dist for this dp
				if currDist < minDist:
					#assign distance to min distance
					minDist = currDist
			#add each datapoint distance to our distance list
			distList.append(minDist)
		#find the max distance in our distance list
		maxDist = max(distList)
		#print(maxDist)
		#find the location of max distance
		locMax = distList.index(maxDist)
		#add datapoint with max distance to the centers list
		Centers.append(data[locMax])
	return(Centers)

finalList = closestCenter(data, Centers)

#this is all formatting
finalStr = ''
for p in finalList:
	for q in p:
		finalStr+= str(q) + ' '
	finalStr+= '\n'

print(finalStr)
outfile.write(finalStr)
outfile.close()


