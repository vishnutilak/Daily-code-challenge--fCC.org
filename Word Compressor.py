def compress(s):
    words = s.split(" ")

    store_dict = {}
    res = []

    for i, word in enumerate(words):
        if word in store_dict:
            res.append(str(store_dict[word]))
        else:
            store_dict[word]=i+1
            res.append(word)
    
    return " ".join(res)
