number_of_students = int(input())
student_info = {}
for student in range(number_of_students):
    student = tuple(input().split())
    name = student[0]
    grade = float(student[1])
    if name not in student_info:
        student_info[name] = []
    student_info[name].append(grade)

for name, grades in student_info.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{grade:.2f}' for grade in grades])}"
    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")

    
    