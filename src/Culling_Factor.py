import numpy as np
import matplotlib.pyplot as plt

def create_leslie_matrix(fertility_rates, survival_rates):
    size = len(fertility_rates)
    leslie_matrix = np.zeros((size, size))
    leslie_matrix[0, :] = fertility_rates 
    for i in range(1, size):
        leslie_matrix[i, i - 1] = survival_rates[i - 1] 
    return leslie_matrix

def simulate_population_growth(initial_population, leslie_matrix, culling_factor, years):
    populations = [initial_population]
    
    for year in range(years):
        current_population = populations[-1]
        next_population = leslie_matrix @ current_population
        
        next_population *= (1 - culling_factor)
        
        populations.append(next_population)
    
    return populations

fertility_rates = np.array([0, 0, 1.6, 1.6, 1.2, 0.3]) 
survival_rates = np.array([0.7, 0.8, 0.9, 0.4, 0.3, 0])  
initial_population = np.array([2250, 1900, 1900, 1350, 725, 300]) 
culling_factor = 1 - 0.8309 
years = 30 

leslie_matrix = create_leslie_matrix(fertility_rates, survival_rates)

populations = simulate_population_growth(initial_population, leslie_matrix, culling_factor, years)

total_population = [np.sum(pop) for pop in populations]

plt.figure(figsize=(10, 6))
plt.plot(range(years + 1), total_population, marker='o')
plt.title('Population Growth Over Time with Culling Factor')
plt.xlabel('Year')
plt.ylabel('Total Population')
plt.grid()
plt.xticks(range(years + 1))
plt.show()

