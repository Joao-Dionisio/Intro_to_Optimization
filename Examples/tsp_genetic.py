
# Adapted from https://www.geeksforgeeks.org/traveling-salesman-problem-using-genetic-algorithm/

from random import random, randint
 
INT_MAX = 9999
# Number of cities in TSP
V = 10
 
# Names of the cities
GENES = "ABCDEFGHIJ"
GENES = GENES[:V]
 
# Starting Node Value
START = 0
 
# Initial population size for the algorithm
POP_SIZE = 10
 
# Structure of a GENOME
# defines the path traversed
# by the salesman while the fitness value
# of the path is stored in an integer
 
class individual:
    def __init__(self) -> None:
        self.genome = ""
        self.fitness = 0
 
    def __lt__(self, other):
        return self.fitness < other.fitness
 
    def __gt__(self, other):
        return self.fitness > other.fitness
 
 
# Function to return a mutated GENOME
# Mutated GENOME is a string
# with a random interchange
# of two genes to create variation in species
def mutatedGene(genome):
    genome = list(genome)
    while True:
        r = randint(1,V-1)
        r1 = randint(1,V-1)
        if r1 != r:
            temp = genome[r]
            genome[r] = genome[r1]
            genome[r1] = temp
            break
    return ''.join(genome)
 
 
# Function to return a valid GENOME string
# required to create the population
def create_genome():
    genome = "0"
    while True:
        if len(genome) == V:
            genome += genome[0]
            break
 
        temp = randint(1,V-1)
        if chr(temp + 48) not in genome:
            genome += chr(temp + 48)
 
    return genome
 
 
# Function to return the fitness value of a genome.
# The fitness value is the path length
# of the path represented by the GENOME.
def cal_fitness(genome):
    mp = [
        [0, 2, INT_MAX, 12, 5],
        [2, 0, 4, 8, INT_MAX],
        [INT_MAX, 4, 0, 3, 3],
        [12, 8, 3, 0, 10],
        [5, INT_MAX, 3, 10, 0],
    ]
    mp = {}
    for i in range(V):
        for j in range(V):
            if random() > 0.1:
                mp[i,j] = randint(1,100)
            else: 
                mp[i,j] = INT_MAX
            mp[j,i] = mp[i,j]

    f = 0
    for i in range(len(genome) - 1):
        if mp[ord(genome[i]) - 48,ord(genome[i + 1]) - 48] == INT_MAX:
            return INT_MAX
        f += mp[ord(genome[i]) - 48,ord(genome[i + 1]) - 48]
 
    return f
 
 
# Function to return the updated value
# of the cooling element.
def cooldown(temp):
    return (90 * temp) / 100
 
 
# Comparator for GENOME struct.
# def lessthan(individual t1,
#               individual t2)
# :
#     return t1.fitness < t2.fitness
 
 
# Utility function for TSP problem.
def TSPUtil(mp):
    # Generation Number
    gen = 1
    # Number of Gene Iterations
    gen_thres = 10
 
    population = []
    temp = individual()
 
    # Populating the GENOME pool.
    for i in range(POP_SIZE):
        temp.genome = create_genome()
        temp.fitness = cal_fitness(temp.genome)
        population.append(temp)
 
    print("\nInitial population: \nGENOME     FITNESS VALUE\n")
    for i in range(POP_SIZE):
        print(population[i].genome, population[i].fitness)
    print()
 
    temperature = 10000
 
    # Iteration to perform
    # population crossing and gene mutation.
    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        print("\nCurrent temp: ", temperature)
        new_population = []
 
        for i in range(POP_SIZE):
            p1 = population[i]
 
            while True:
                new_g = mutatedGene(p1.genome)
                new_genome = individual()
                new_genome.genome = new_g
                new_genome.fitness = cal_fitness(new_genome.genome)
 
                if new_genome.fitness <= population[i].fitness:
                    new_population.append(new_genome)
                    break
 
                else:
                    # Accepting the rejected children at
                    # a possible probability above threshold.
                    prob = pow(
                        2.7,
                        -1
                        * (
                            (float)(new_genome.fitness - population[i].fitness)
                            / temperature
                        ),
                    )
                    if prob > 0.5:
                        new_population.append(new_genome)
                        break
 
        temperature = cooldown(temperature)
        population = new_population
        print("Generation", gen)
        print("GENOME     FITNESS VALUE")
 
        total_fitness = 0
        for i in range(POP_SIZE):
            print(population[i].genome, population[i].fitness)
            total_fitness += population[i].fitness
        print("Mean fitness: %i" % (total_fitness/len(population)))
        gen += 1
 
 
if __name__ == "__main__":

    mp = {}
    for i in range(V):
        for j in range(V):
            if random() > 0.1:
                mp[i,j] = randint(1,100)
            else: 
                mp[i,j] = INT_MAX
            mp[j,i] = mp[i,j]
    TSPUtil(mp)