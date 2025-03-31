
start_interval = int(input())

end_interval = int(input())

magic_num = int(input())
combination_counter = 0
magic_condition = False
for first_num in range(start_interval, end_interval + 1):
    for second_num in range(start_interval, end_interval + 1):
        combination_counter += 1
        if first_num + second_num == magic_num:
            magic_condition = True
            print(f"Combination N:{combination_counter} ({first_num} + {second_num} = {magic_num})")

    if magic_condition:
        break

else:
    print(f"{combination_counter} combinations - neither equals {magic_num}")


