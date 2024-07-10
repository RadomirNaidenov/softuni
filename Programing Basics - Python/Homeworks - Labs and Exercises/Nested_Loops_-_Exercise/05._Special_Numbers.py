n = int(input())

for current_num in range(1111, 10000):

    current_num_as_str = str(current_num)

    is_special = True
    for d in current_num_as_str:
        digit = int(d)

        if digit == 0:
            is_special = False
            break

        if n % digit != 0:
            is_special = False
            break
    if is_special:
        print(current_num, end=" ")












