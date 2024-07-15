def checking_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_winning_symbol in winning_symbols:
        for uninterrupted_winning_symbol_length in range(10, 5, -1):
            winning_symbol_repetition = current_winning_symbol * uninterrupted_winning_symbol_length
            if winning_symbol_repetition in left_part and winning_symbol_repetition in right_part:
                if uninterrupted_winning_symbol_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_winning_symbol_length}{current_winning_symbol} Jackpot!'

                return f'ticket "{ticket}" - {uninterrupted_winning_symbol_length}{current_winning_symbol}'

    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for current_ticket in tickets:
    print(checking_ticket(current_ticket))


