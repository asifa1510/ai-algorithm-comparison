import random
import math
from hill_climbing import hill_climbing

def random_restart_hill_climbing(restarts, step_size,iterations_per_run):
    best_solution = Nonebest_value= float('-inf')
    
    for _ in range(restarts):
        start= random.uniform(0,10)
        solution, value= hill_climbing(start, step_size,iterations_per_run)
        
        if value> best_value:
            best_solution, best_value= solution, value
            
            
        return best_solution, best_value
    
if __name__ == "__main__":
    best_x, best_y = random_restart_hill_climbing(
        restarts=10,
        step_size=0.1,
        iterations_per_run=1000
    )
    print(f"Best solution after restarts: x = {best_x:.4f}, f(x) = {best_y:.4f}")
