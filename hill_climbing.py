import random
import math

def objective_function(x):
    return x* math.sin(x)

def hill_climbing(start, step_size, iterations):
    current= start
    current_val= objective_function(current)
    
    for _ in range(iterations):
        neighbor= current+ random.uniform(-step_size, step_size)
        neighbor_val = objective_function(neighbor)
        
        if neighbor_val> current_val:
            current, current_val= neighbor, neighbor_val
        
        return current, current_val
    
if __name__ =="__main__":
    best_x, best_y = hill_climbing(start=random.uniform(0, 10), step_size=0.1, iterations=1000)
    print(f"Best solution: x = {best_x:.4f}, f(x) = {best_y:.4f}")
