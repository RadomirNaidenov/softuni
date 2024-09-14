def age_assignment(*args, **kwargs):
    result = {}
    for kay, value in kwargs.items():
        for name in args:
            if kay in name:
                result[name] = value
    result = dict(sorted(result.items(), key=lambda item: item[0]))
    
    final_result = ""
    for name, age in result.items():            
        final_result += f"{name} is {age} years old.\n"

    return final_result

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))