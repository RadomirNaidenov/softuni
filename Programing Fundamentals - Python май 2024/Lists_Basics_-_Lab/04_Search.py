n = int(input())
word = input()
my_list = []

for _ in range(n):
    current_str = input()
    my_list.append(current_str)

print(my_list)

for elements in my_list:
    if word not in elements:
        my_list.remove(elements)
print(my_list)



