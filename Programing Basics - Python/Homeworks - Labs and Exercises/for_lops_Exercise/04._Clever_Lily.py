lily_age = int(input())
washing_machine = float(input())
price_for1_toy = int(input())
toys_count = 0

budget = 0

for birthday in range(1, lily_age + 1):
    if birthday % 2 == 0:
        birthday_money = birthday * 5
        budget += birthday_money
        budget -= 1
    else:
        toys_count += 1

budget += price_for1_toy * toys_count

if budget >= washing_machine:
    diff = budget - washing_machine
    print(f"Yes! {diff:.2f}")
else:
    diff = washing_machine - budget
    print(f"No! {diff:.2f}")


