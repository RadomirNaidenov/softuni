tournament_count = int(input())
starting_point = int(input())
gained_pints = 0
count_wins = 0
for _ in range(tournament_count):
    reach_stage = input()

    if reach_stage == "W":
        gained_pints += 2000
        count_wins += 1
    elif reach_stage == "F":
        gained_pints += 1200
    elif reach_stage == "SF":
        gained_pints += 720

total_point = starting_point + gained_pints
average_point = gained_pints / tournament_count
percent_wins = count_wins / tournament_count * 100
print(f"Final points: {total_point}")
print(f"Average points: {int(average_point)}")
print(f"{percent_wins:.2f}%")


