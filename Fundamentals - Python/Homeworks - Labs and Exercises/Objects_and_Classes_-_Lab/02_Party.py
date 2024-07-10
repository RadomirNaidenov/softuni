class Party:

    def __init__(self):
        self.party_list = []


party = Party()
names = input()
while True:

    if names == "End":
        break

    party.party_list.append(names)
    names = input()

print(f"Going: {", ".join(party.party_list)}")
print(f"Total: {len(party.party_list)}")