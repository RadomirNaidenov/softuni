def softuni_students(*args, **kwargs):
    students = {}
    invalid_students = []
    for course_id, username in args:
        if course_id not in kwargs:
            invalid_students.append(username)
            continue

        students[username] = course_id
    
    output = []
    sorted_by_username = dict(sorted(students.items()))
    for username, course_id in sorted_by_username.items():
        course_name = kwargs[course_id]
        result = f"*** A student with the username {username} has successfully finished the course {course_name}!"
        output.append(result)

    if invalid_students:
        invalid_students_result = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        output.append(invalid_students_result)

    return "\n".join(output)




