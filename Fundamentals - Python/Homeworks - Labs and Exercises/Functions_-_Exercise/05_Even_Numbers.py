def is_even(current_number):
    return current_number % 2 == 0


number_as_string = input().split()
number_as_digits = []
for number in number_as_string:
    number_as_digits.append(int(number))
final_list = list(filter(is_even, number_as_digits))
print(final_list)

