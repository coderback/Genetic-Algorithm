import random
import copy
import pandas as pd
import math

# Define Parameters
d = 20
N = d + 1  # Number of genes in an individual
P = 100  # Size of the population
MUTRATE = 0.1  # Mutation rate
MUTSTEP = 0.1  # Size of alterations during mutation
GENS = 50  # Number of generations
NUM_RUNS = 10  # Number of runs
MIN = -10
MAX = 10  # Generate the initial population with real-valued genes

# Lists to store results for each run
final_average_fitness_data = []
final_best_fitness_data = []

# Lists to store mean values
mean_average_fitness_data = []
mean_best_fitness_data = []


# Define an individual as a class
class Individual:
    def __init__(self):
        self.genes = [0.0] * N  # Initialize genes as a list of real numbers
        self.fitness = 0  # Initialize fitness as zero


# Define a test function that calculates the utility based on genes
def test_function(ind):
    n = len(ind.genes)
    sum_part = sum(i * (2 * ind.genes[i] ** 2 - ind.genes[i - 1]) ** 2 for i in range(2, n))
    return (ind.genes[0] - 1) ** 2 + sum_part


# Main loop for multiple runs
for run in range(NUM_RUNS):
    # Reset population for each run
    population = []
    for _ in range(P):
        tempgene = [random.uniform(MIN, MAX) for _ in range(N)]
        newind = Individual()  # Create a new individual
        newind.genes = tempgene  # Set its genes to the generated genes
        population.append(newind)  # Add the individual to the population list

    # Lists to store fitness data for plotting
    average_fitness_data = []
    best_fitness_data = []

    # Main loop for evolving the population
    for generation in range(0, GENS):
        offspring = []
        # Select parents and create offspring
        for i in range(0, P):
            parent1 = random.randint(0, P - 1)
            off1 = copy.deepcopy(population[parent1])
            parent2 = random.randint(0, P - 1)
            off2 = copy.deepcopy(population[parent2])
            if test_function(off1) < test_function(off2):
                offspring.append(off1)
            else:
                offspring.append(off2)

        # Crossover
        for i in range(0, P, 2):
            toff1 = copy.deepcopy(offspring[i])
            toff2 = copy.deepcopy(offspring[i + 1])
            temp = copy.deepcopy(offspring[i])
            crosspoint = random.randint(1, N)
            for j in range(crosspoint, N):
                toff1.genes[j] = toff2.genes[j]
                toff2.genes[j] = temp.genes[j]
            offspring[i] = copy.deepcopy(toff1)
            offspring[i + 1] = copy.deepcopy(toff2)

        # Mutation
        for i in range(0, P):
            newind = Individual()
            newind.genes = []
            for j in range(0, N):
                gene = offspring[i].genes[j]
                mutprob = random.random()
                if mutprob < MUTRATE:
                    gene += random.uniform(-MUTSTEP, MUTSTEP)
                newind.genes.append(gene)
            offspring[i] = copy.deepcopy(newind)

        # Calculate fitness for the offspring
        for i in range(0, P):
            offspring[i].fitness = test_function(offspring[i])

        # Update the population with the offspring
        population = copy.deepcopy(offspring)

        # Calculate and record average fitness and best fitness for the current generation
        total_fitness = sum(ind.fitness for ind in population)
        average_fitness = total_fitness / P
        best_fitness = min(ind.fitness for ind in population)

        average_fitness_data.append(average_fitness)
        best_fitness_data.append(best_fitness)

        print(
            f"Run {run + 1}, Generation {generation + 1}: Average Fitness = {average_fitness}, Best Fitness = {best_fitness}")

    # Store results for the final generation of the current run
    final_average_fitness_data.append(average_fitness_data[-1])
    final_best_fitness_data.append(best_fitness_data[-1])

# Calculate mean values
mean_average_fitness = sum(final_average_fitness_data) / NUM_RUNS
mean_best_fitness = sum(final_best_fitness_data) / NUM_RUNS

# Create a DataFrame to store results
results_df = pd.DataFrame({
    'Run': range(1, 11),
    'Final Average Fitness': final_average_fitness_data,
    'Final Best Fitness': final_best_fitness_data,
})

# Add mean values to the DataFrame
results_df.loc['Mean'] = ["Average", mean_average_fitness, mean_best_fitness]

# Save results to Excel file
excel_file_path = 'genetic_algorithm_results.xlsx'
results_df.to_excel(excel_file_path, index=False)

print(f"Results saved to {excel_file_path}")
