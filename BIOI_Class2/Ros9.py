#Ros9.py
#quinn thomas
#Rosalind 9
import random

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "Ros9Pract.txt", 'r').read().splitlines()
#create output file
outfile = open(mydir + 'Ros9.txt', 'w')


def createDict(infile):
	myDict = {}
	count = 0
	for item in infile:
		#print(item)
		keys=item[0]
		values = item[5:]
		#print(values)
		myDict.setdefault(keys, [])
		for x in values.split(','):
			#print(x)
			count +=1
			myDict[keys].append(x)
	return myDict, count

#this is the number of edges that should exist
myDict, count = createDict(infile)
#print(count)
#print(myDict)


def pathway(myDict):
	
	firstitem = list(myDict.items())[cycleStart]
	#currItem = firstitem

	nodes = list(myDict.keys())
	print(nodes)
	#we need two lists, one to keep track of the cycle
	#and one to keep track of the nodes that have been used
	random_start = random.randint(0,len(nodes)-1)
	print(random_start)
	cycle = []
	#current_cycle = [nodes[random_start]]
	
	while nodes:
		currItem = firstitem[-1]
		if myDict[currItem]:
			nextItem = myDict[currItem].pop()
			current_cycle.append(nextItem)
		else:
			cycle.append(current_cycle.pop())
	cycle = cycle.reverse()
	cycle = '->'.join(final)
	return cycle






'''
		#if our current item in the dictionary is not a dead end
		if currItem in dictionary:
			#append the curren item to our list of nodes
			nodes.append(currItem)
			if len(dictionary[currItem])>1:
				lastBranch = currItem
				cycle += nodes
				nextItem = random.randint(0,len(dictionary[currItem])-1)

			nextItem = random.randint(0,len(dictionary[currItem])-1)
			temp = deepcopy(currItem)
			currItem = dictionary.items()[currItem][nextItem]
			deleted[currItem] = dictionary[currItem][nextItem]
			dictionary[temp].remove(currItem)

'''


pathway(myDict)

