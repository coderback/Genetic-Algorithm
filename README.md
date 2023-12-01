# Genetic-Algorithm
This repository contains a Python implementation of a basic Genetic Algorithm (GA) designed for my Artificial Intelligence II Course at UWE, Bristol
The GA evolves a population of individuals over a specified number of generations, with each individual represented as a vector of real-valued genes. The optimization task is defined by a user-defined test function in this case is a minimalisation fitness function, and the algorithm aims to find individuals with low fitness.

## Key Features
Population Representation: Individuals are represented as classes with real-valued genes.  
Selection: Parents are randomly selected from the current population.  
Crossover: Two-point crossover is applied to pairs of individuals in the offspring.  
Mutation: Random alterations are made to individual genes based on a mutation rate.  
Fitness Calculation: The fitness of each individual is determined by a user-defined test function.  
Visualization: Fitness progression is visualized over generations using Matplotlib.  

## Usage
Clone the repository: git clone https://github.com/coderback/genetic-algorithm.git  
Install dependencies: pip install matplotlib  
Run the GA script: minimalisation_function.py  

## Results
The script records and prints average fitness and best fitness for each generation. The best individual in the final population is also identified and displayed.

## Visualization
Fitness progression is visualized using Matplotlib, providing insights into the algorithm's performance over generations.
