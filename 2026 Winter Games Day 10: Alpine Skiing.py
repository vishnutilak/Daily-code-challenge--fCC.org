def get_hill_rating(drop, distance, hill_type):

    steepness = drop/distance
    adj_steepness =1
    if hill_type=="Downhill":
        adj_steepness = steepness*1.2
    elif hill_type=="Slalom":
        adj_steepness = steepness*0.9
    else:
        adj_steepness = steepness

    
    if adj_steepness<=0.1:
        return "Green"
    elif adj_steepness<=0.25:
        return "Blue"
    else:
        return "Black"
