def title_case(title):
    words = title.split(" ")
    result = []

    for w in words:
        if w:
            result.append(w[0].upper() + w[1:].lower())

    return " ".join(result)
