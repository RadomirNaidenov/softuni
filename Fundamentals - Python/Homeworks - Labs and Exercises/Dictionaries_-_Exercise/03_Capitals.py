country_names = input().split(", ")
capital_cities = input().split(", ")
dictionary = dict(zip(country_names, capital_cities))

for country, capital in dictionary.items():
    print(f"{country} -> {capital}")
