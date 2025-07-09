import random
import math

def objective_function(x):
    return x* math.sin(x)

def simulated_annealing(start, step_size, initial_temp,cooling_rate,iterations):
    current= start
    current_val =objective_function(current)
    temp= initial_temp
    
    for _ in range(iterations):
        neighbor= current+random.uniform(-step_size, step_size)
        neighbor_val=objective_function(neighbor)
        
        delta= neighbor_val- current_val
        
        if delta>0 or random.uniform(0,1)< math.exp(delta/temp):
            current, current_val = neighbot, neighbor_val
        
        temp *= cooling_rate
    
    return current, current_val
if __name__ ="__main__":
    best_x, best_y = simulated_annealing(
        start=random.uniform(0, 10),
        step_size=0.5,
        initial_temp=100,
        cooling_rate=0.98,
        iterations=1000
    )
    print(f"Best solution: x = {best_x:.4f}, f(x) = {best_y:.4f}")
    