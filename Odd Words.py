def get_odd_words(s):
    all_words = s.split(" ")
    
    res =[]
    for word in all_words:
        if len(word)%2==1:
            res.append(word)

    return " ".join(res)
