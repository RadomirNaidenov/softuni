command = input()
total_steps = 0
while command != "Going home":
    current_steps = int(command)
    total_steps += current_steps

    if total_steps >= 10000:
        break

    command = input()
if command == "Going home":
    current_steps = int(input())
    total_steps += current_steps

is_goal_reached = total_steps >= 10000
if is_goal_reached:
    diff = total_steps - 10000
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    diff = 10000 - total_steps
    print(f"{diff} more steps to reach goal.")