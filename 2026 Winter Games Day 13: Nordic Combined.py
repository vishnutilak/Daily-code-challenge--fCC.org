def calculate_start_delays(jump_scores):
    best = jump_scores[0]
    for jump in jump_scores:
        if jump>best:
            best = jump
    delays =[]

    for score in jump_scores:
        diff = best- score
        float_delay = diff*1.5

        delay = int(float_delay)
        if float_delay >delay:
            delay+=1
        
        delays.append(delay)

    return delays
