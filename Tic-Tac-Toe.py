def tic_tac_toe(board):
    lines =[]
    #rows
    for i in range(3):
        lines.append(board[i])
    #cols
    for j in range(3):
        lines.append([board[0][j],board[1][j],board[2][j]])
    #negdiag
    lines.append([board[0][0], board[1][1], board[2][2]])
    #posdiag
    lines.append([board[2][0], board[1][1], board[0][2]])
    for line in lines:
        if line[0]==line[1]==line[2]:
            return f"{line[0]} wins"
    return "Draw"
