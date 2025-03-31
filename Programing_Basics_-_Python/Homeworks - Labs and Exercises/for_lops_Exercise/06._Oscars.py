name_actor = input()
point_of_academy = float(input())
judges_count = int(input())

total_point = point_of_academy

for _ in range(judges_count):
    name_judges = input()
    judges_point = float(input())
    current_point = len(name_judges) * judges_point / 2
    total_point += current_point
    if total_point > 1250.5:
        break

if total_point > 1250.5:
    print(F"Congratulations, {name_actor} got a nominee for leading role with {total_point:.1f}!")
else:
    diff = 1250.5 - total_point
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
