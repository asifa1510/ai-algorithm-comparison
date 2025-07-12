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
    return random.choices(population, weights=probs, k=2)

def genetic_algorithm(bounds=(0,10), population_size= 20,generations=100, mutation_rate=0.1):
    population= [create_individual(bounds) for _ in range(population_size)]
    
    for _ in range(generations):
        fitnesses=[ objective_function(ind) for ind in population]
        new_population=[]
        
    
        for _ in range(population_size):
            parent1, parent2= select_parents(population, fitnesses)
            child= crossover(parent1, parent2)
            child= mutate(child, mutation_rate, bounds)
            child= max(bounds[0], min(bounds[1], child))
            new_population.append(child)
            
        population= new_population
        
    best = max(population, key=objective_function)
    return best, objective_function(best)

if __name__ == "__main__":
    best_x, best_y = genetic_algorithm()
    print(f"Best solution: x = {best_x:.4f}, f(x) = {best_y:.4f}")

