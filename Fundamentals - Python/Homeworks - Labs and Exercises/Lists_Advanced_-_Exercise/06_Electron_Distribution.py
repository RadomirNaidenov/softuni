def electrons_transfer(electrons):
    shells = []
    number_of_shells = 1
    while electrons > 0:
        max_electrons = 2 * number_of_shells ** 2
        if electrons >= max_electrons:
            shells.append(max_electrons)
            electrons -= max_electrons
        else:
            shells.append(electrons)
            electrons = 0
        number_of_shells += 1

    return shells


number_of_electrons = int(input())
filled_shells = electrons_transfer(number_of_electrons)
print(filled_shells)

