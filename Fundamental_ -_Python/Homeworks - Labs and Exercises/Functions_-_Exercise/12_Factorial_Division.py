def calculate_number(some_number:int) -> int:
    for current_num in range(1, some_number):
        some_number *= current_num
    return some_number


first_number = int(input())
second_number = int(input())
first_factorial = calculate_number(first_number)
second_factorial = calculate_number(second_number)
print(f"{first_factorial / second_factorial:.2f}")
