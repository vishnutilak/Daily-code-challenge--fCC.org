def find_pawn_moves(pos: str) -> list[str]:
    file = pos[0]
    rank = int(pos[1])

    moves = []

    if rank < 8:
        moves.append(file + str(rank + 1))
        if rank == 2:
            moves.append(file + str(rank + 2))

    return moves
