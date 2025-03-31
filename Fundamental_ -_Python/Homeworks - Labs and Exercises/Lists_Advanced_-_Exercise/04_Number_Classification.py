def return_positive_numbers(some_numbers):
    positive_number = [int(num) for num in numbers if int(num) >= 0]
    positive_number = ", ".join(map(str, positive_number))
    return f"Positive: {positive_number}"


def return_negative_numbers(some_numbers):
    negative_number = [int(num) for num in some_numbers if int(num) < 0]
    negative_number = ", ".join(map(str, negative_number))
    return f"Negative: {negative_number}"


def return_even_numbers(some_numbers):
    even_number = [int(num) for num in some_numbers if int(num) % 2 == 0]
    even_number = ", ".join(map(str, even_number))
    return f"Even: {even_number}"


def return_odd_numbers(some_numbers):
    odd_numbers = [int(num) for num in some_numbers if int(num) % 2 != 0]
    odd_numbers = ", ".join(map(str, odd_numbers))
    return f"Odd: {odd_numbers}"


numbers = input().split(", ")
print(return_positive_numbers(numbers))
print(return_negative_numbers(numbers))
print(return_even_numbers(numbers))
print(return_odd_numbers(numbers))