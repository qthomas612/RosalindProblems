#Ros20.py
#quinn thomas
#Rosalind 20
import os
import math

#identify the directory you are working in
mydir = "/Users/QuinnThomas/Desktop/BIOI_500/"
#save input file to variable and read by lines
infile = open(mydir + "rosalind_ba10c.txt", 'r').readlines()
#create output file
outfile = open(mydir + 'Ros20.txt', 'w')

#separate all the variables from input
string = infile[0].strip()
sigma = infile[2].strip().split()
states = infile[4].strip().split()

print(string)
print(sigma)
print(states)

transition_values = []
#formatting transition values matrix
count= 7
for line in infile[7:]:
    line = line.strip().split()
    print(line)
    if len(line) ==1:
        break
    transition_values.append(line[1:])
    count+=1
print("transition matrix: ", transition_values)

emission_values = []
#formatting emission values matrix
for line in infile[count+2:]:
    line = line.strip().split()
    #print(line)
    emission_values.append(line[1:])
print("emission matrix: ", emission_values)
#print("string: ", string)


#transition matrix
#       A       B
# A   0.641   0.359
# B   0.729   0.271


#emission matrix
#       x       y       z
# A   0.117   0.691   0.192   
# B   0.097   0.42    0.483


#initialize s matrix
s=[]
mini_matrix=[]
first_letter= string[0]
lett_idx = sigma.index(first_letter)
for k in range(len(states)):
    value = 0.5*float(emission_values[k][lett_idx])
    mini_matrix.append(value)
    
#print(mini_matrix)
s.append(mini_matrix)


def makeMatrix(s, t_mat, e_mat, prev_mat):
    #start with values in transition matrix
    arrow_matrix = []
    #for the length of the string
    for i in range(1,len(string)):
        #identify our current character
        curr_letter = string[i]
        #current index tells us which column we need to look in our emission matrix
        curr_idx = sigma.index(curr_letter)
        #print("index  of letter: ", curr_idx)
        mini_mat = []
        mini_arrows = []
        for each in states:
            max_val = 0
            q = states.index(each)
            #print("index of state: ", q)
            for j in range(len(states)):
                #first multiply previous with transition values
                val1 = float(prev_mat[j])
                val2 = float(t_mat[j][q])
                val_prod = val1*val2
                if val_prod > max_val:
                    max_val = val_prod
                    arrow = j
            #now that we have a max value we need to multiply by 
            #the emission value
            mini_mat.append(max_val*float(e_mat[q][curr_idx]))
            mini_arrows.append(arrow)
        #print(mini_mat)
        s.append(mini_mat)
        arrow_matrix.append(mini_arrows)
        prev_mat = mini_mat
    return s, arrow_matrix
                
    
s_matrix, arrows = makeMatrix(s, transition_values, emission_values, mini_matrix)
#print(s_matrix)
#print(arrows)

#find max value in last column and where it came from
max_index = s_matrix[-1].index(max(s_matrix[-1]))
#print(max_index)

state_list = []
state_list.append(max_index)

#traceback from our max value using indexes
for mini in reversed(arrows):
    row = mini[max_index]
    state_list.append(row)
    max_index=row
print(state_list)

#change our ones and zeroes to the letters from states
state_str = ''
for val in state_list:
    state = states[val]
    state_str+=state
#reverse our string
state_str=state_str[::-1]
print(state_str)
print(string)
#print(len(state_str))

outfile.write(state_str)
outfile.close()




