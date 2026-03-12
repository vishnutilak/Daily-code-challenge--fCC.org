def convert_words(s):
    words = s.split(" ")
    result =[]

    for word in words:
        result.append(str(len(word)))

    return " ".join(result)

# return " ".join(str(len(word)) for word in words)
