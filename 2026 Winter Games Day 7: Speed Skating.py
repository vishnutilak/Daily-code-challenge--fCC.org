def largest_difference(skater1, skater2):
    max_diff = 0.0
    best_lap = 1

    for i in range(len(skater1)):
        diff = abs(skater1[i]-skater2[i])
        if diff>max_diff:
            max_diff = diff
            best_lap = i+1

    return best_lap
