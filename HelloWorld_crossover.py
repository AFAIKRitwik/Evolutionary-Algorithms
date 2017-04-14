'''
The aim of this program is to develop an Evolutionary algorithm to generate the target words using crossovers and mutations
'''

import random
import string

class HelloWorld(object):
    # Class Variables
    def __init__(self):
        self.target = "My First program"
        self.GENE_SIZE = 300
        self.population = []

    # Defining the fitness function
    '''
    parent - changes after each iteration
    target - defined above

    '''
    def fitness(self, parent,target):
        fitness_value = 0 #Best fit
        self.parent = parent
        for i in range(0,len(parent)):
            fitness_value = fitness_value + (ord(self.target[i])-ord(parent[i]))**2
        return fitness_value

    '''
    Create  a Gene pool. i.e. initial population.
    This replaces the initial string or source and replaces it with random parents
    GENE_SIZE is the number of elements in the initial population

    '''
    def generatePopulation(self):
        for i in range(0,self.GENE_SIZE):
            # selects the chromosome from a random set of printable characters and limits it to len(target)
            chromosome = [random.choice(string.printable[:-10]) for j in range(0,len(self.target))]
            thisFitness = self.fitness(chromosome, self.target)
            selectedParent = {'chromosome':chromosome, 'fitness':thisFitness}
            self.population.append(selectedParent)
            print "---"
            print i, ''.join(self.population[i]['chromosome'])

    def crossover(self,parent1,parent2):
        parent1 = parent1
        parent2 = parent2

        #set the decendent as having same characteristics as parent1
        childChromosome = parent1['chromosome'][:]

        #Select 2 random positions in chromosome of parent 2 to splice this cut area with the gene copied from parent 1
        startPosition = random.randint(0,len(parent2['chromosome'])-1)
        stopPosition = random.randint(0,len(parent2['chromosome'])-1)
        if startPosition > stopPosition:
            startPosition,stopPosition = stopPosition,startPosition

        #perform splice
        childChromosome[startPosition:stopPosition] = parent2['chromosome'][startPosition:stopPosition]

        # now mutate a random base of the child chromosome
        randPosition = random.randint(0,len(childChromosome)-1)
        childChromosome[randPosition] = chr(ord(childChromosome[randPosition]) + random.randint(-1,1))
        childFitness = self.fitness(childChromosome,self.target)
        return({'chromosome':childChromosome,'fitness':childFitness})

    def randomParent(self,population):
        #select a random parent from the population. Use uniform product distribution. Q: Why ?
        randomValue = int(random.random() * random.random() * (self.GENE_SIZE-1))
        return (population[randomValue])

    def main(self):
        self.generatePopulation()
        i=0
        while True:
            i=i+1
            self.population.sort(key = lambda selectedParent: selectedParent['fitness'])
            if self.population[0]['fitness'] == 0:
                print "Target Reached!"
                print "size of the population is : %i" %(len(self.population))
                break
            parent1 = self.randomParent(self.population)
            parent2 = self.randomParent(self.population)

            child  = self.crossover(parent1,parent2)
            if child['fitness']< self.population[-1]['fitness']:
                self.population[-1] = child

            print "%5i %s" %(i,''.join(child['chromosome']))

if __name__ == '__main__':
    a = HelloWorld()
    a.main()
