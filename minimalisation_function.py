import random
import copy
import matplotlib.pyplot as plt
import math

# Define Parameters
d = 20
N = d + 1  # Number of genes in an individual
P = 100  # Size of the population
MUTRATE = 0.1  # Mutation rate
MUTSTEP = 0.1  # Size of alterations during mutation
GENS = 50  # Number of generations
MIN = -10  # Generate the initial population with real-valued genes(Lowest possible value)
MAX = 10  # Generate the initial population with real-valued genes(Highest possible value)

# Lists to store the population and offspring
population = []  # Initialize the population list
offspring = []  # Initialize the offspring list


# Define an individual as a class
class Individual:
    def __init__(self):
        self.genes = [0.0] * N  # Initialize genes as a list of real numbers
        self.fitness = 0  # Initialize fitness as zero


for _ in range(P):
    tempgene = [random.uniform(MIN, MAX) for _ in range(N)]
    newind = Individual()  # Create a new individual
    newind.genes = tempgene  # Set its genes to the generated genes
    population.append(newind)  # Add the individual to the population list


# Define a test function that calculates the utility based on genes
def test_function(ind):
    n = len(ind.genes)
    sum_part = sum(i * (2 * ind.genes[i] ** 2 - ind.genes[i - 1]) ** 2 for i in range(2, n))
    return (ind.genes[0] - 1) ** 2 + sum_part


# Lists to store fitness data for plotting
average_fitness_data = []
best_fitness_data = []

# Main loop for evolving the population
for generation in range(0, GENS):
    offspring.clear()
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

    print(f"Generation {generation + 1}: Average Fitness = {average_fitness}, Best Fitness = {best_fitness}")

# Find and print the best individual in the final population
best_individual = min(population, key=lambda ind: ind.fitness)
print("Best Individual - Genes:", best_individual.genes)
print("Best Individual - Fitness:", best_individual.fitness)

generations = list(range(1, GENS + 1))
plt.figure(figsize=(10, 5))
plt.plot(generations, average_fitness_data, label='Average Fitness', marker='o')
plt.plot(generations, best_fitness_data, label='Best Fitness', marker='o')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.title('Genetic Algorithm Fitness Progression')
plt.grid(True)
plt.show()
