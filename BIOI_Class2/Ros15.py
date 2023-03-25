#Ros15.py
#quinn thomas
#Rosalind 15
import os
import math

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba8b.txt", 'r').readlines()
#create output file
outfile = open(mydir + 'Ros15.txt', 'w')

k = int(infile[0][0])
dim = int(infile[0][2])

#print(k)
#print(dim)

Centers = []
data = []

count = 1

#formatting the input file
for line in infile[1:]:
	line = line.strip().split()
	if len(line) == 1:
		for q in infile[count+1:]:
			q = q.strip().split()
			emptynList =[]
			for la in q:
				la = float(la)
				emptynList.append(la)
			data.append(emptynList)
		break
	else:
		emptyList = []
		for num in line:
			num = float(num)
			emptyList.append(num)
		Centers.append(emptyList)
		count+=1

#print(data)
#print(Centers)

def distance(m, cp, dp):
	sum = 0
	for r in range(len(cp)):
		sum+=(dp[r]-cp[r])**2
	#print(sum)
	dist = math.sqrt(sum)
	return dist


def closestCenter(data, Centers):
	distList = []
	for i in data:
		minDist = float('inf')
		#for each center point
		for j in Centers:	
			# find the distance between the datapoint and center point
			currDist = distance(dim, j, i)
			#if our distance is less than the minimum dist for this dp
			if currDist < minDist:
				#assign distance to min distance
				minDist = currDist
		distList.append(minDist)
	return(distList)

listDist = closestCenter(data, Centers)
print(listDist)

#square each value in distance list
for d in range(len(listDist)):
	new = listDist[d]**2
	listDist[d] = new

#divide the sum of distances by number of datapoints to get distortion
answer = sum(listDist)/len(data)
#format
answer = format(answer, '.3f')
print(answer)

outfile.write(str(answer))
outfile.close()





