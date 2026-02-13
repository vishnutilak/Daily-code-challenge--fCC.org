def compute_score(judge_scores, *penalties):
    highest = judge_scores[0]
    lowest = judge_scores[0]

    total =0

    for score in judge_scores:
        total+=score

        if score<lowest:
            lowest = score
        if score >highest:
            highest = score
    base_score = total- highest-lowest
    
    for p in penalties:
        base_score -=p
    
    return base_score
