rows = int(input())
my_list = []
for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    my_list.extend(numbers)

print(my_list)

