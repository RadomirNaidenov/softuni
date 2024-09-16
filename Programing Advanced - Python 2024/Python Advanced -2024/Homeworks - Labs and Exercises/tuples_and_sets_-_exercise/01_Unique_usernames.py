number_of_usernames = int(input())
names = []

for _ in range(number_of_usernames):
    name = input()
    if name in names:
        continue
    names.append(name)

names = tuple(names)
for name in names:
    print(name)

    
    
