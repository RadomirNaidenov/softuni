from math import ceil
number_of_people = int(input())
capacity_elevator = int(input())

courses = number_of_people / capacity_elevator
print(ceil(courses))
