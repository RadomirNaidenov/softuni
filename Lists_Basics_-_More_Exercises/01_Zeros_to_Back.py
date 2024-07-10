def move_zero_to_back(some_integers):
    none_zero_number = [num for num in some_integers if num != 0]
    zero_number = [num for num in some_integers if num == 0]

    result = none_zero_number + zero_number

    return result

input_string = input().split(", ")
integer_input = [int(num) for num in input_string]
result = move_zero_to_back(integer_input)
print(result)








