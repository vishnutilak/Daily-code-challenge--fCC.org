def create_board(dimensions):
    rows, cols = dimensions
    board =[]

    for r in range(rows):
        row =[]
        for c in range(cols):
            if (r+c)%2 ==0:
                row.append("X")
            else:
                row.append("O")
        board.append(row)

    return board
