
def passing_count(scores, passing_score):

    # count = 0
    # for score in scores:
    #     if score>=passing_score:
    #         count+=1
    # return count

    return sum(score>=passing_score for score in scores)
