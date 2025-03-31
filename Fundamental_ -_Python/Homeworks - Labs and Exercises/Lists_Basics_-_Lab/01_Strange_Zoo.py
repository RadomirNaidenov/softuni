my_list = []

for _ in range(3):
    word = input()
    my_list.append(word)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)