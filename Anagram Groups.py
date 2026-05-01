def group_anagrams(words):
    groups = {}

    for word in words:
        count = [0]*26
        for ch in word:
            count[ord(ch)-ord('a')] +=1
        key = tuple(count)

        if key not in groups:
            groups[key]=[]
        groups[key].append(word)

    return list(groups.values())
