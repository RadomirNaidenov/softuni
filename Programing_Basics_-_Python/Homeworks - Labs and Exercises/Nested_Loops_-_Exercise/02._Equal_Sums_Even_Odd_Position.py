first_number = int(input())
second_name = int(input())

for number in range(first_number, second_name + 1):
    number_to_string = str(number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")
