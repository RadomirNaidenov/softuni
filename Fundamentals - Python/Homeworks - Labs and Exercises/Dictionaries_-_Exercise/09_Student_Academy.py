num = int(input())
name_and_grade = {}
for _ in range(num):
    name = input()
    grade = float(input())

    if name not in name_and_grade.keys():
        name_and_grade[name] = 0
        name_and_grade[name] += grade

    else:
        name_and_grade[name] += grade
        average_grade = name_and_grade[name] / 2
        name_and_grade[name] = average_grade

for name, average_grade in name_and_grade.items():
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")





