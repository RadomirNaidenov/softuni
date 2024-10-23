def list_roman_emperors(*args, **kwargs):

    successful_emperors = []
    unsuccessful_emperors = []

    for emperor_info in args:
        name, is_successful = emperor_info
        rule_length = kwargs.get(name)

        if rule_length is not None:
            if is_successful:
                successful_emperors.append((name, rule_length))
            else:
                unsuccessful_emperors.append((name, rule_length))

    successful_emperors.sort(key=lambda x: (-x[1], x[0]))

    unsuccessful_emperors.sort(key=lambda x: (x[1], x[0]))

    output = []
    total_emperors = len(successful_emperors) + len(unsuccessful_emperors)
    output.append(f"Total number of emperors: {total_emperors}")

    if successful_emperors:
        output.append("Successful emperors:")
        for name, length in successful_emperors:
            output.append(f"****{name}: {length}")

    if unsuccessful_emperors:
        output.append("Unsuccessful emperors:")
        for name, length in unsuccessful_emperors:
            output.append(f"****{name}: {length}")

    return '\n'.join(output)


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14, ))