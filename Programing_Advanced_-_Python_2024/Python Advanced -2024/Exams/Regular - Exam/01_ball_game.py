from collections import deque


def main(strength: list[int], accuracy: deque[int]) -> str:
    total_goals = 0
    output = []
    while strength and accuracy:
        current_strength = strength.pop()
        current_accuracy = accuracy.popleft()

        total_sum = current_strength + current_accuracy

        if total_sum == 100:
            total_goals += 1

        elif total_sum < 100:
            if current_strength > current_accuracy:
                strength.append(current_strength)
            elif current_strength < current_accuracy:
                accuracy.append(current_accuracy)
            elif current_strength == current_accuracy:
                strength.append(total_sum)

        elif total_sum > 100:
            current_strength -= 10
            if current_strength > 0:
                strength.append(current_strength)
            accuracy.append(current_accuracy)

    if not total_goals:
        output.append("Paul failed to score a single goal.")
    elif total_goals and total_goals == 3:
        output.append("Paul scored a hat-trick!")
    elif total_goals and total_goals > 3:
        output.append("Paul performed remarkably well!")
    elif total_goals and total_goals < 3:
        output.append("Paul failed to make a hat-trick.")

    if total_goals:
        output.append(f"Goals scored: {total_goals}")
    if strength:
        output.append(f"Strength values left: {', '.join([str(x) for x in strength])}")
    if accuracy:
        output.append(f"Accuracy values left: {', '.join([str(x) for x in accuracy])}")

    print("\n".join(output))
    
main(
    [int(x) for x in input().split(" ")],
    deque([int(x) for x in input().split(" ")])

)







