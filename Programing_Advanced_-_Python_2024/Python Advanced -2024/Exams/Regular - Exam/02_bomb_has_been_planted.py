def counter_terrorist_simulation():
    dimensions = input().strip().split(', ')
    N = int(dimensions[0])
    M = int(dimensions[1])

    game_map = [list(input().strip()) for _ in range(N)]

    ct_pos = None
    bomb_pos = None
    time_left = 16
    game_over = False

    for i in range(N):
        for j in range(M):
            if game_map[i][j] == 'C':
                ct_pos = (i, j)
            elif game_map[i][j] == 'B':
                bomb_pos = (i, j)

    initial_ct_pos = ct_pos

    while time_left > 0 and not game_over:
        command = input().strip()

        if command in ["left", "right", "up", "down"]:
            new_ct_pos = update_position(ct_pos, command, N, M)
            x, y = new_ct_pos
            old_x, old_y = ct_pos

            if game_map[x][y] == 'T':
                game_map[old_x][old_y] = '*'
                print("Terrorists win!")
                game_over = True
            elif game_map[x][y] == 'B':
                ct_pos = (x, y)
            else:

                ct_pos = new_ct_pos
                game_map[old_x][old_y] = '*'
                game_map[x][y] = 'C'

            time_left -= 1

        elif command == "defuse":
            if ct_pos == bomb_pos:
                if time_left >= 4:
                    time_left -= 4
                    game_map[ct_pos[0]][ct_pos[1]] = 'D'
                    print("Counter-terrorist wins!")
                    print(f"Bomb has been defused: {time_left} second/s remaining.")
                    game_over = True
                else:
                    game_map[ct_pos[0]][ct_pos[1]] = 'X'
                    print("Terrorists win!")
                    print("Bomb was not defused successfully!")
                    print(f"Time needed: {4 - time_left} second/s.")
                    game_over = True
            else:
                time_left -= 2

    if not game_over:
        game_map[ct_pos[0]][ct_pos[1]] = '*'
    game_map[initial_ct_pos[0]][initial_ct_pos[1]] = 'C'

    for row in game_map:
        print("".join(row))


def update_position(position, direction, N, M):
    x, y = position
    if direction == "left":
        if y > 0:
            return (x, y - 1)
    elif direction == "right":
        if y < M - 1:
            return (x, y + 1)
    elif direction == "up":
        if x > 0:
            return (x - 1, y)
    elif direction == "down":
        if x < N - 1:
            return (x + 1, y)
    return position


counter_terrorist_simulation()
