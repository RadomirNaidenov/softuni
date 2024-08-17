rows, columns = [int(x) for x in input().split()]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(alphabet)
matrix = []
for row in range(rows):
    matrix_row = []
    for col in range(columns):
        first_last_letter = alphabet[row]
        middle_index = (row + col) % num_letters
        middle_letter = alphabet[middle_index]

        palindrome = first_last_letter + middle_letter + first_last_letter
        matrix_row.append(palindrome)

    matrix.append(matrix_row)

for row in matrix:
    print(" ".join(row))