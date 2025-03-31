needed_money = float(input())
available_money = float(input())
consecutive_spend_days = 5
days = 0

while consecutive_spend_days:
    action = input()
    money = float(input())
    days += 1

    if action == 'spend':
        available_money -= money
        consecutive_spend_days -= 1

        if available_money < 0:
            available_money = 0

    elif action == 'save':
        available_money += money
        consecutive_spend_days = 5
        if available_money >= needed_money:
            print(f'You saved the money for {days} days.')
            break

else:
    print("You can't save the money.")
    print(days)
