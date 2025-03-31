len_of_sets = input().split()
first_set_len = int(len_of_sets[0])
second_set_len = int(len_of_sets[1])
first_set = set()
second_set = set()

for _ in range(first_set_len):
    number = int(input())
    first_set.add(number)

for _ in range(second_set_len):
    number = int(input())
    second_set.add(number)

elements_in_both = first_set.intersection(second_set)
for element in elements_in_both:
    print(element)
