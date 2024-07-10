money_as_string = input().split(",")
number_of_beggars = int(input())
money_as_integer = []

for money in money_as_string:
    money_as_integer.append(int(money))

final_list = []
start_index = 0

for current_beggars in range(number_of_beggars):
    current_beggars_sum = 0

    for current_index in range(start_index, len(money_as_integer), number_of_beggars):
        current_beggars_sum += money_as_integer[current_index]
    final_list.append(current_beggars_sum)
    start_index += 1
print(final_list)
