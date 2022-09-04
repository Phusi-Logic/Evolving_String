import time
import random
import matplotlib.pyplot as plt
letters = 'abcdefghijklmnopqrstuvwxyz,.  '  # Include extra space at the end to prevent any list/string range problems


def make_first_genotype(first_phenotype):
    first_genotype = []
    for n in range(0, len(first_phenotype)):
        first_genotype.append(0)
    return first_genotype


def mutate(genotype, number_of_mutations=1):
    mutated_genotype = genotype.copy()
    for n in range(0, number_of_mutations):
        which_part = random.randint(0, len(genotype)-1)
        what_value = random.randint(0, len(letters)-1)
        mutated_genotype[which_part] = what_value
    return mutated_genotype


def make_phenotype(genotype):
    phenotype_string = ""
    for i in genotype:
        phenotype_string = phenotype_string + letters[i]
    return phenotype_string


def make_genotype(phenotype):
    genotype_list = []
    for l in phenotype:
        genotype_list.append(letters.index(l))
    return genotype_list


def check_fitness(phenotype, perfect_phenotype):
    local_fitness_factor = 0
    for n, letter in enumerate(phenotype):
        if phenotype[n] == perfect_phenotype[n]:
            local_fitness_factor += 1
    return local_fitness_factor


def make_offspring_array(phenotype, number_of_offspring, mutations=True, number_of_mutations=1):
    offspring_array = []
    for i in range(0, number_of_offspring):
        offspring_genes = make_genotype(phenotype)
        if mutations is True:
            offspring_genes = mutate(offspring_genes, number_of_mutations)
        offspring = make_phenotype(offspring_genes)
        offspring_array.append(offspring)
    return offspring_array


def selection(phenotype_array, perfect_phenotype):
    fitness_dict = {}
    for n, each_phenotype in enumerate(phenotype_array):
        fitness_test = check_fitness(each_phenotype, perfect_phenotype)
        fitness_dict[each_phenotype] = fitness_test
    return max(fitness_dict, key=fitness_dict.get)


# Setup conditions
number_of_generations = 1000
number_of_offspring_per_generation = 50
number_of_mutations_per_offspring = 1

# First generation
perfect_phenotype = "I think it inevitably follows, " \
                    "that as new species in the course of time are formed through natural selection, " \
                    "others will become rarer and rarer, and finally extinct."
current_genotype = make_first_genotype(perfect_phenotype)
current_phenotype = make_phenotype(current_genotype)
fitness_factor = check_fitness(current_phenotype, perfect_phenotype)
generation = 0
# Print all factors
print("generation: ", generation,
      " fitness: ", fitness_factor,
      "   phenotype: ", current_phenotype,
      " genotype: ", current_genotype)

# Make arrays for data for matplotlib
gen_data = [0]
fitness_data = [fitness_factor]

for generation in range(1, number_of_generations):
    # Produce offspring and let the fittest survive
    offspring_population = make_offspring_array(current_phenotype,
                                                number_of_offspring_per_generation,
                                                mutations=True,
                                                number_of_mutations=number_of_mutations_per_offspring)
    current_phenotype = selection(offspring_population, perfect_phenotype)
    # Set the factors to be printed
    current_genotype = make_genotype(current_phenotype)
    fitness_factor = check_fitness(current_phenotype, perfect_phenotype)
    # Print all factors
    print("generation: ", generation,
          " fitness: ", fitness_factor,
          "   phenotype: ", current_phenotype,
          " genotype: ", current_genotype)
    # Get each generations data
    gen_data.append(generation)
    fitness_data.append(fitness_factor)
    time.sleep(0.1)  # delay to make the change more visible

# Plot the data with matplotlib
plt.plot(gen_data, fitness_data)
plt.xlabel('number of generations')
plt.ylabel('fitness')
plt.show()
