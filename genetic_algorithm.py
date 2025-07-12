import random
import math

def objective_function(x):
    return x* math.sin(x)

def create_individual(bounds):
    return random.uniform(*bounds)

def mutate(individual, mutation_rate, bounds):
    if random.random() < mutation_rate:
        return individual + random.uniform(-0.5,0.5)
    return individual
def crossover(parent1,parent2):
    return (parent1+parent2)/2

def select_parents(population, fitnesses):
    total=sum(fitnesses)
    probs=[f/total for f in fitnesses]


