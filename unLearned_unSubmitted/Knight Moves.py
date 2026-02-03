def knight_moves(pos: str) -> int:
    x = ord(pos[0]) - ord('A') + 1
    y = int(pos[1])

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    count = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            count += 1

    return count
