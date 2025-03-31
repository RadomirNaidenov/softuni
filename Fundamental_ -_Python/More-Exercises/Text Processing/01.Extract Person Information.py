n = int(input())
datas = [input() for _ in range(n)]

for data in datas:
    start_name_index = data.find("@") + 1
    end_name_index = data.find("|")
    name = data[start_name_index:end_name_index]
    start_age_index = data.find("#") + 1
    end_age_index = data.find("*")
    age = data[start_age_index:end_age_index]

    print(f"{name} is {age} years old.")