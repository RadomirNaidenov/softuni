number = input().split()
absolute_valley_list = []

for current_num in number:
    absolute_valley_list.append(abs(float(current_num)))

print(absolute_valley_list)

