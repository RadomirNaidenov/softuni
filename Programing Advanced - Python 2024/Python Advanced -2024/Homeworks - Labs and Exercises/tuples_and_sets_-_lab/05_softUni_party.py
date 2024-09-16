n = int(input())  
vip_guests = []
regular_guests = []

for _ in range(n):
    reservation_code = input().strip()
    if reservation_code[0].isdigit():
        vip_guests.append(reservation_code)
        continue
    regular_guests.append(reservation_code)


while True:
    guest = input().strip()
    if guest == "END":
        break
    if guest in vip_guests:
        vip_guests.remove(guest)
    elif guest in regular_guests:
        regular_guests.remove(guest)

vip_guests.sort()
regular_guests.sort()

remaining_guests = vip_guests + regular_guests

print(len(remaining_guests))
for guest in remaining_guests:
    print(guest)




