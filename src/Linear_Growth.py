import numpy as np
import matplotlib.pyplot as plt

def leslie_growth(leslie_matrix, initial_population, C, time_steps):
    population = np.array(initial_population)
    
    total_population_over_time = [population.sum()]  

    total_population = population.sum()
    k = (total_population + C) / total_population 

    for _ in range(time_steps):
        population = np.dot(leslie_matrix, population)
        population *= k * 0.8309
        total_population_over_time.append(population.sum())
        total_population = population.sum()
        k = (total_population + C) / total_population 
    return total_population_over_time
leslie_matrix = np.array([[0, 0, 1.6, 1.6, 1.2, 0.3], 
                           [0.7, 0, 0, 0, 0, 0], 
                           [0, 0.8, 0, 0, 0, 0],
                           [0, 0, 0.9, 0, 0, 0],
                           [0, 0, 0, 0.4, 0, 0],
                           [0, 0, 0, 0, 0.3, 0]])
initial_population = [2250, 1900, 1900, 1350, 725, 300]  
C = 50
time_steps = 30  

total_population_over_time = leslie_growth(leslie_matrix, initial_population, C, time_steps)

plt.figure(figsize=(10, 6))
plt.plot(total_population_over_time, marker='o', color='b')

plt.title('Total Population Dynamics over Time with Leslie Matrix')
plt.xlabel('Time Steps')
plt.ylabel('Total Population')
plt.grid(True)
plt.xticks(range(len(total_population_over_time))) 
plt.show()

