def calculate_penalty_distance(rounds):

    penalty =0

    for hit in rounds:
        penalty +=int(150 *(5-hit))

    return penalty
