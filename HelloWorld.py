'''
The aim of this program is to develop an Evolutionary algorithm to generate the target words using simple mutations
'''

import random

target = "Hello World!"
source = "1234567890 ," #Question: should the source always have the same no of letters? Ans: Not necessarly. This is just my first example.


# Defining the fitness function
'''
parent - changes after each iteration
target - defined above

'''
def fitness(parent,target):
    fitness_value = 0 #Best fit
    for i in range(0,len(parent)):
        fitness_value = fitness_value + abs(ord(target[i])-ord(parent[i]))
    return fitness_value
'''

Mutation
Logic:
    1. Pick a random position in parent
    2. convert the string into a list of characters
    3. increment / decrement random parent character position by a random value between 26 and -26
    4. join the list of characters into a single string
    * Mutates only a single character
'''
def mutate(parent):
    selectedPosition = random.randint(0,len(parent)-1)#select a random position
    makeListOfParent = list(parent)
    testCond = ord(makeListOfParent[selectedPosition])+random.randint(-26,26)
    condition = False
    while condition == False:
        if (testCond >=30 or testCond <= 123):
            makeListOfParent[selectedPosition] = chr(testCond)
            condition = True
        else:
            condition = False
            testCond = ord(makeListOfParent[selectedPosition])+random.randint(-26,26)

    return(''.join(makeListOfParent))


def mainProgram(source,target):
    fitnessValue = fitness(source,target)
    i=0
    while True:
        i=i+1
        mutation = mutate(source)
        fitnessValueOfMutation = fitness(mutation,target)
        if fitnessValueOfMutation < fitnessValue:
            fitnessValue = fitnessValueOfMutation
            source = mutation
            print "%5i %5i %s " %(i,fitnessValueOfMutation,mutation)
        else:
            if i%50000 == 0:
                print i
        if fitnessValue == 0:
            break

#calling the main program from python terminal
mainProgram(source,target)
