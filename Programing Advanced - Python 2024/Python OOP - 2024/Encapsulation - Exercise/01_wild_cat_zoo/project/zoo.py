class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[str] = []
        self.workers: list[str] = []

    def add_animal(self, animal, prise) -> str:
        is_capacity_left = self.__animal_capacity > len(self.animals)
        is_budget_left = self.__budget >= prise
        if is_capacity_left and is_budget_left:
            self.__budget -= prise
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if is_capacity_left and not is_budget_left:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        all_salaries = sum(x.salary for x in self.workers)
        if self.__budget >= all_salaries:
            self.__budget -= all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        all_money_for_take_care = sum(x.money_for_care for x in self.animals)
        if self.__budget >= all_money_for_take_care:
            self.__budget -= all_money_for_take_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self) -> str:
        result = [f"You have {len(self.animals)} animals"]

        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(lion.__repr__())

        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(tiger.__repr__())

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(cheetah.__repr__())

        return "\n".join(result)

    def workers_status(self) -> str:
        result = [f"You have {len(self.workers)} workers"]

        keeps = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result.append(f"----- {len(keeps)} Keepers:")
        for keep in keeps:
            result.append(keep.__repr__())

        result.append(f"----- {len(caretakers)} Caretakers:")
        for care_taker in caretakers:
            result.append(care_taker.__repr__())

        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(vet.__repr__())

        return "\n".join(result)











