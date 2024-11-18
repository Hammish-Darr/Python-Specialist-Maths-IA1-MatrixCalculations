import numpy as np
import matplotlib.pyplot as plt

def leslie_growth(leslie_matrix, initial_population, years):
    population = np.array(initial_population)
    
    total_population_over_years = [population.sum()]  
    
    for _ in range(years):
        population = np.dot(leslie_matrix, population)
        
        total_population_over_years.append(population.sum())
    
    return total_population_over_years

leslie_matrix = np.array([[0, 0, 1.6, 1.6, 1.2, 0.3],  
                           [0.7, 0, 0, 0, 0, 0],  
                           [0, 0.8, 0, 0, 0, 0],
                           [0, 0, 0.9, 0, 0, 0],
                           [0, 0, 0, 0.4, 0, 0],
                           [0, 0, 0, 0, 0.3, 0]])
initial_population = [2250, 1900, 1900, 1350, 725, 300]  
years = 30  

total_population_over_years = leslie_growth(leslie_matrix, initial_population, years)


plt.figure(figsize=(10, 6))
plt.plot(total_population_over_years, marker='o', color='b')

plt.title('Total Population Dynamics Over Years with Leslie Matrix')
plt.xlabel('Years')
plt.ylabel('Total Population')
plt.grid(True)
plt.xticks(range(len(total_population_over_years))) 
plt.show()
