def find_left_handed_seats(table):
    rows = 2
    cols = 4
    count =0

    for r in range(rows):
        for c in range(cols):
            if table[r][c] != "U":
                continue

            if r == 0:
                if c <cols-1 and table[r][c + 1] == "R":
                    continue

            else:
                if c >0 and table[r][c - 1]== "R":
                    continue
            count += 1
    
    return count
