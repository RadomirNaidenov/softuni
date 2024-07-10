group_count = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0
for _ in range(1, group_count + 1):
    num_people = int(input())

    if num_people <= 5:
        group_1 += num_people
    elif 6 <= num_people <= 12:
        group_2 += num_people
    elif 13 <= num_people <= 25:
        group_3 += num_people
    elif 26 <= num_people <= 40:
        group_4 += num_people
    else:
        group_5 += num_people

total_people = group_1 + group_2 + group_3 + group_4 + group_5

percent_group_1 = group_1 / total_people * 100
percent_group_2 = group_2 / total_people * 100
percent_group_3 = group_3 / total_people * 100
percent_group_4 = group_4 / total_people * 100
percent_group_5 = group_5 / total_people * 100

print(f"{percent_group_1:.2f}%")
print(f"{percent_group_2:.2f}%")
print(f"{percent_group_3:.2f}%")
print(f"{percent_group_4:.2f}%")
print(f"{percent_group_5:.2f}%")