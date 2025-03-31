from collections import deque


def main(monsters_armors: deque[int], soldiers_striking_impact: [list[int]]):
    killed_monsters = 0
    while monsters_armors and soldiers_striking_impact:
        current_monster_armor = monsters_armors.popleft()
        current_soldier_strike_impact = soldiers_striking_impact.pop()

        if current_soldier_strike_impact >= current_monster_armor:
            current_soldier_strike_impact -= current_monster_armor
            killed_monsters += 1
            if current_soldier_strike_impact:
                if soldiers_striking_impact:
                    soldiers_striking_impact[-1] += current_soldier_strike_impact
                    continue
                soldiers_striking_impact.append(current_soldier_strike_impact)
        else:
            current_monster_armor -= current_soldier_strike_impact
            monsters_armors.append(current_monster_armor)

    if not monsters_armors:
        print("All monsters have been killed!")
    if not soldiers_striking_impact:
        print("The soldier has been defeated.")
    print(f"Total monsters killed: {killed_monsters}")


main(
    deque([int(x) for x in input().split(",")]),
    [int(x) for x in input().split(",")]
)

