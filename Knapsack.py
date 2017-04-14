# Evolutionary approach to solve the 0/1 knapsack problem
'''
AIM OF EA: EVOLVE EACH CANDIDATE TO BECOME A VALID SOLUTION

Each object is represented as a list of 3 values. [item_no, weight, value,True]
objlist = list of objects
the knapsack is considered as the chromosome
knapsack = actual final knapsack. represented as a list of objects along with the corresponding firness function.
knapsack = [objlist, existing_weight, benefit_value, fitness_value]
            where
                existing_weight = sum of all weights in knapsack
                Weight_fitness_value = capacity - existing_weight in knapsack. 0 is Best 
                benefit_value = sum of all object values in knapsack
                benefit_fitness = ?
mutation - randomly flipping the toggle value from False to True and vice versa.

Logic -

    1. select some random elements and include in knapsack such that the total weight is <= capacity
    2. Keep track of the elements selected for the best benefit so far
    3. continue for 3000 runs and select the best combination so far

Note: The gene pool always consists of both parents and children. No selection of parents is done here

'''

import random
import string
from sys import exit

class knapsack(object):
    def __init__(self):
        self.objlist = []
        self.knapsack = [[],1,1,1]
        self.benefit_value = 0
        self.weight_fitness_value = 0
        self.existing_weight = 0
        self.element_no = []
        self.bestknapsack = [[],1000,1000,1000]

    '''
    count  the total number of available elements
    capacity  the total capacity of the knapsack
    '''
    def initialization(self,count,capacity):
        self.count = count
        self.capacity = capacity
        for i in range (0,self.count):
            self.item = [i,random.randint(1,50),random.randint(1,20),False]
            print self.item,"\n"
            self.objlist.append(self.item)
        #print self.objlist

    '''
    Mutation involves flipping a random item from True to False and vice versa.
    (i.e) selecting a random item


    '''
    def mutation(self,objectList):
        mutatedObject = objectList
        #perform mutation a random no of times
        mutateCount = random.randint(0,len(objectList)-1)
        for i in range(0,mutateCount-1):
            #Randomly select a chromosome
            selectedChromosome = random.randint(0,len(objectList)-1)
            #flip the true / false bit of the chromosome
            if mutatedObject[selectedChromosome][3] == False:
                mutatedObject[selectedChromosome][3] = True
            else:
                mutatedObject[selectedChromosome][3] =False
        return mutatedObject

    def selectElements(self,objectlist):
        '''
        Select and place into the knapsack all items that are flagged "True"
        '''
        self.benefit_value = 0
        self.existing_weight = 0
        self.knapsack = []
        self.element_no=[]
        for i in range (0,len(objectlist)):
            if objectlist[i][3] == True:
                self.benefit_value = self.benefit_value  + objectlist[i][2]
                self.existing_weight = self.existing_weight + objectlist[i][1]
                self.element_no.append(objectlist[i][0])
                self.knapsack = [self.element_no,self.existing_weight,self.benefit_value,999]
        return self.knapsack

    def fitness(self,knapsack):
        if self.knapsack[3] > 0 :# best fit
            self.weight_fitness_value = 0
            self.weight_fitness_value = self.capacity - knapsack[1]
            if self.weight_fitness_value >= 0 :
                self.knapsack[3] = (self.weight_fitness_value)
        #print "Weight: ",self.knapsack[1],"   Value: ",self.knapsack[2],"  Fitness: ",self.knapsack[3]
        #print "knapsack[0]=  ",self.knapsack[0]

        print self.knapsack
        if self.knapsack[3] == 0:
            self.bestknapsack = self.knapsack
            print "best knapsack = ",self.bestknapsack
            #exit(0)
        return self.knapsack

    def init2(self, capacity):
        '''
        This is just a test class containing 4 items
        Total capacity of knapsack = 5
        Solution : items 1,2 - MAx weight = 5, max benefit = 7
        Item # Weight Value
        1       2       3
        2       3       4
        3       4       5
        4       5       6

        '''
        self.capacity = capacity
        self.objlist = [1,2,3,False],[2,3,4,False],[3,4,5,False],[4,5,6,False]


    def main(self):
        #self.initialization(10,250) #init(count_of_elements, capacity_of_knapsack)
        #print self.objlist
        self.init2(5)

        for i in range(0,1000):
            self.max = 000 # a random large value chosen arbitrarly
            self.objlist = self.mutation(self.objlist)
            #print self.objlist
            self.knapsack = self.selectElements(self.objlist)
            if len(self.knapsack)>0:
                self.knapsack[0] = list(set(self.knapsack[0]))
                self.knapsack = self.fitness(self.knapsack)
                if self.knapsack[1]>self.max:
                    if self.knapsack[2] <= self.capacity:
                        self.max = self.knapsack[1]
                        self.bestknapsack = self.knapsack
                        w=i
                        print "best knapsack: ", self.bestknapsack
                '''if self.knapsack[2]<=self.capacity:
                    if self.knapsack[1]>self.max:
                        self.max = self.knapsack[1]
                        self.bestknapsack = self.knapsack
                    '''#print self.knapsack
        print "The Final Best: ", self.bestknapsack, "in iteration: ",w

        # stop program after 100 generations


        return 0




if __name__ == '__main__':
    a = knapsack()
    a.main()
