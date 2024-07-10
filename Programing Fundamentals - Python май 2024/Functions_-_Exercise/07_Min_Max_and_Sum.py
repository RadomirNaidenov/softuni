def min_number(numbers):
    return min(numbers)


def max_number(number):
    return max(number)


def sum_numbers(number):
    return sum(number)


numbers_as_string = input().split()
number_as_digits = [int(number) for number in numbers_as_string]
print(f"The minimum number is {(min_number(number_as_digits))}")
print(f"The maximum number is {(max_number(number_as_digits))}")
print(f"The sum number is: {(sum_numbers(number_as_digits))}")