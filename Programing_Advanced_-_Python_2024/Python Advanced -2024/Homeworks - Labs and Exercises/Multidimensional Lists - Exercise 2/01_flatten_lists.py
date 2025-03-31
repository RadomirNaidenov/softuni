sublists = input().split("|")
sublists = sublists[::-1]

flattened_lst = []

for sublist in sublists:
    flattened_lst.extend(sublist.split())

flattened_lst = [int(num) for num in flattened_lst if num]

print(*flattened_lst)
