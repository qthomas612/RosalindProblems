#Ros16.py
#quinn thomas
#Rosalind 16
import os
import math

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba8c.txt", 'r').readlines()
#create output file
outfile = open(mydir + 'Ros16.txt', 'w')

k = int(infile[0][0])
m = int(infile[0][2])


data =[]

#formatting
for line in infile[1:]:
	line =line.strip().split(" ")
	emptyList = []
	for num in line:
		num = float(num)
		emptyList.append(num)
	data.append(emptyList)

Centers = data[0:k]
print(Centers)

def distance(m, cp, dp):
	sum = 0
	for r in range(len(cp)):
		sum+=(dp[r]-cp[r])**2
	#print(sum)
	dist = math.sqrt(sum)
	return dist

def closestCenter(d, c):
	#this time our distance list is going to be the centers each
	#data point is associated with
	centerTracker = []
	#print(Centers)
	#distList = []
	for r in d:
		count = 0
		minDist = float('inf')
		#for each center point
		for j in c:
			#print(j)
			# find the distance between the datapoint and center point
			currDist = distance(m, j, r)
			#if our distance is less than the minimum dist for this dp
			if currDist < minDist:
				#assign distance to min distance
				minDist = currDist
				currCount = count
			count+=1
		#print('\n')

		centerTracker.append(currCount)
		#distList.append(minDist) #old code
	return(centerTracker)

# this function adds all m coordinates and calculates the center of gravity
def mathFunction(eachList):
	newCenter = []
	#h is the coordinate that we are currently summing
	for h in range(m):
		mysum = 0
		for item in eachList:
			mysum+= item[h]
		point = mysum/len(eachList)
		point = format(point, '.3f')
		newCenter.append(float(point))
	return newCenter


def main(cents, dat):
	newCenters = []
	#print(Centers)
	#x = 0
	while True:
		#print(Centers)
		centerIdxs = closestCenter(dat, cents)
		#print(centerIdxs)
		#print("This is m: ", m)
		for t in range(k):
			#find the indexes for each data point so we can map
			#data points to centers
			indices = [i for i, x in enumerate(centerIdxs) if x == t]
			#print(indices)
			smallList = []
			#create a mini list of data points for each center
			for each in indices:
				smallList.append(data[each])
			#print(smallList)
			#send mini list to find the center of gravity
			dp = mathFunction(smallList)
			#add all new centers of gravity to the newCenters list
			newCenters.append(dp)
		
		#print(Centers)
		#print(newCenters)
		#print('\n')
		#check to see if the Centers of gravity reached convergence
		if cents == newCenters:
			return cents
		#if not prepare variables for the loop
		else:
			cents = newCenters
			newCenters = []
			

unformatted = main(Centers, data)
#print(unformatted)

#formatting
answer =''
for item in unformatted:
	for i in range(m):
		point = item[i]
		point = format(point, '.3f')
		answer += str(point)+' '
	answer += '\n'
print(answer)

outfile.write(answer)
outfile.close()



