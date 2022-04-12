import random
class Gene:
    def __init__(self):
        value_list = [0,1]      
        self.value = random.choice(value_list)
    def flip(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0
    def __repr__(self):
        return str(self.value)
class Chromosome:
    def __init__(self):
        self.genes = [Gene() for i in range(10)]
    def mutate(self):
        for gene in self.genes:
            random_number = random.randint(0,101)
            if random_number > 70: 
                gene.flip()
    def __repr__(self):
        return str(self.genes)
    def __str__(self):
        return str(self.genes)
class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for i in range(1)]
    def mutate(self):
        for chromosome in self.chromosomes:
            random_number = random.randint(0,101)
            if random_number > 70: 
                chromosome.mutate()    
    def __repr__(self):
        return_repr = "\nDNA SEQUENCE:\n"
        for chromosome in self.chromosomes:
            return_repr += str(chromosome) + "\n"
        return return_repr
class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment
        self.mutate_probability = random.randint(0,101)
    
    def mutate(self):
        random_number = random.randint(0,101)
        if random_number > self.mutate_probability:
            self.dna.mutate()
    def check_ones(self):     
        for chromo in self.dna.chromosomes:
            result = all(gene.value == 1 for gene in chromo.genes)
            if result == False:
                return False
        return True
human_dna = DNA()
human = Organism(human_dna, "Human")
cycles = 0
while human.check_ones() == False:
    human.mutate()
    cycles += 1
    print(human.dna)
print("Cycles to get ALL ones:",cycles)