players = {}

while True:
    command = input()
    if command == "Season end":
        break

    if " -> " in command:
        
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}
        
        if position not in players[player]:
            players[player][position] = skill
        else:
            if players[player][position] < skill:
                players[player][position] = skill

    elif " vs " in command:
        
        player1, player2 = command.split(" vs ")

        if player1 in players and player2 in players:
            common_position = False

            for position in players[player1]:
                if position in players[player2]:
                    common_position = True
                    break
            
            if common_position:
                total_skill_player1 = sum(players[player1].values())
                total_skill_player2 = sum(players[player2].values())

                if total_skill_player1 > total_skill_player2:
                    del players[player2]
                elif total_skill_player2 > total_skill_player1:
                    del players[player1]


player_stats = []
for player in players:
    total_skill = sum(players[player].values())
    player_stats.append((player, total_skill))


for i in range(len(player_stats)):
    for j in range(i + 1, len(player_stats)):
        if (player_stats[i][1] < player_stats[j][1]) or (player_stats[i][1] == player_stats[j][1] and player_stats[i][0] > player_stats[j][0]):
            player_stats[i], player_stats[j] = player_stats[j], player_stats[i]


for player, total_skill in player_stats:
    print(f"{player}: {total_skill} skill")

    positions = list(players[player].items())

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if (positions[i][1] < positions[j][1]) or (positions[i][1] == positions[j][1] and positions[i][0] > positions[j][0]):
                positions[i], positions[j] = positions[j], positions[i]

    for position, skill in positions:
        print(f"- {position} <::> {skill}")

