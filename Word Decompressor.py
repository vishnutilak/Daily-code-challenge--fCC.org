def decompress(s):

    words = s.split(" ")

    store_dict = {}
    res = []

    for i, word in enumerate(words):
        if word.isdigit():
            res.append(store_dict[int(word)])
        else:
            store_dict[i+1]=word
            res.append(word)
    
    return " ".join(res)
