judges_count = int(input())
command = input()
total_score = 0
total_grades = 0
while command != "Finish":
    current_presentations = command

    current_presentations_total = 0
    for _ in range(judges_count):
        current_score = float(input())
        current_presentations_total += current_score

    avg_score = current_presentations_total / judges_count
    print(f"{current_presentations} - {avg_score:.2f}.")
    total_score += current_presentations_total
    total_grades += judges_count
    command = input()

avg_total_score = total_score / total_grades
print(f"Student's final assessment is {avg_total_score:.2f}.")

