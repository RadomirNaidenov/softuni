course_info = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in course_info.keys():
        course_info[course_name] = []
    course_info[course_name].append(student_name)


for course_name, registered_students in course_info.items():
    print(f"{course_name}: {len(registered_students)}")
    print('\n'.join(f"-- {student}" for student in registered_students))
