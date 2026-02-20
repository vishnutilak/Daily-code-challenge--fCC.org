def check_eligibility(athlete_weights, sled_weight):
    n = len(athlete_weights)

    if n==1:
        min_sled=162
        max_weight= 247
    elif n==2:
        min_sled=170
        max_weight= 390
    elif n==4:
        min_sled=210
        max_weight= 630
    else:
        return "Not Eligible"

    if sled_weight< min_sled:
        return "Not Eligible"
    
    total_weight=0
    for w in athlete_weights:
        total_weight += w
    combined_weight = total_weight+ sled_weight

    if combined_weight> max_weight:
        return "Not Eligible"
    
    return "Eligible"
