class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals_list = []
        self.fishes_list = []
        self.birds_list = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals_list.append(name)

        elif species == "fish":
            self.fishes_list.append(name)

        elif species == "bird":
            self.birds_list.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            species_list = self.mammals_list

        elif species == "fish":
            species_list = self.fishes_list

        elif species == "bird":
            species_list = self.birds_list

        else:
            return "Invalid species"

        return f"{species.capitalize()}s in {self.name}: {", ".join(species_list)}\nTotals animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)


species_to_get_info = input()
print(zoo.get_info(species_to_get_info))
