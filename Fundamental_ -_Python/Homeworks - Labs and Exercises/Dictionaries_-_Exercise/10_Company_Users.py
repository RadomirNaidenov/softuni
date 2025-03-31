names_and_id = {}
while True:
    command = input()
    if command == "End":
        break

    company_name, employess_id = command.split(" -> ")
    if company_name not in names_and_id.keys():
        names_and_id[company_name] = []
    if employess_id not in names_and_id[company_name]:
        names_and_id[company_name].append(employess_id)

for company_name, employes_id in names_and_id.items():
    print(company_name)
    print('\n'.join(f"-- {x}" for x in names_and_id[company_name]))

