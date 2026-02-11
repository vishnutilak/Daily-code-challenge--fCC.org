def get_landing_stance(start_stance, rotation):

    flips = abs(rotation) // 180
    #every 180- theres one flip


    #even case
    if flips%2==0:
        return start_stance
    #odd case
    if start_stance == "Regular":
        return "Goofy"
    else:
        return "Regular"
