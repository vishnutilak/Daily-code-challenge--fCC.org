def score_curling(board):
    stones = []  # will store tuples like ("R", ring_number)

    for r in range(5):
        for c in range(5):
            cell = board[r][c]

            if cell == '.':
                continue  # skip empty spaces

            # Determine ring based on position
            if r == 2 and c == 2:
                ring = 0  # center button
            elif abs(r - 2) <= 1 and abs(c - 2) <= 1:
                ring = 1  # immediate neighbors around center
            else:
                ring = 2  # outer ring

            stones.append((cell, ring))

    # Separate rings by team
    r_rings = []
    y_rings = []

    for team, ring in stones:
        if team == "R":
            r_rings.append(ring)
        else:
            y_rings.append(ring)

    # If one team has no stones, other team scores all their stones
    if not r_rings and not y_rings:
        return "No points awarded"

    if not r_rings:
        return "Y: " + str(len(y_rings))

    if not y_rings:
        return "R: " + str(len(r_rings))

    closest_r = min(r_rings)
    closest_y = min(y_rings)

    # Same closest distance → no score
    if closest_r == closest_y:
        return "No points awarded"

    # Determine winner and threshold
    if closest_r < closest_y:
        winner = "R"
        threshold = closest_y
        count = 0
        for ring in r_rings:
            if ring < threshold:
                count += 1
        return "R: " + str(count)

    else:
        winner = "Y"
        threshold = closest_r
        count = 0
        for ring in y_rings:
            if ring < threshold:
                count += 1
        return "Y: " + str(count)
