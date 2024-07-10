open_tab_browser = int(input())
salary = int(input())


for tab_number in range(open_tab_browser):

    tab = input()

    if tab == 'Facebook':
        salary -= 150

    elif tab == 'Instagram':
        salary -= 100

    elif tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break

else:
    print(salary)


