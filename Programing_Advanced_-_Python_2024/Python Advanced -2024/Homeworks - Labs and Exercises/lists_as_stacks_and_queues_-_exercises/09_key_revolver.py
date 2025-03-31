from collections import deque

price_of_bullet = int(input())
gun_barrel = int(input())
bullets = [int(bullet) for bullet in input().split()]
targets = deque([int(lock) for lock in input().split()])
value_of_the_intelligence  = int(input())
bullets_shot = 0

while bullets and targets:
    bullet_damage = bullets.pop()
    if targets[0] >= bullet_damage:
        targets.popleft()
        print("Bang!")
    else:
        print("Ping!")
    bullets_shot += 1
    if bullets_shot % gun_barrel == 0 and bullets:
        print("Reloading!")

if not targets:
    earned_money = value_of_the_intelligence  - (bullets_shot * price_of_bullet)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
else:
    print(f"Couldn't get through. Locks left: {len(targets)}")