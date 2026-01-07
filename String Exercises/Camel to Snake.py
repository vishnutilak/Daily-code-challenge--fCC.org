def to_snake(s):
    result = ""

    for ch in s:
        if ch.isupper():
            result += "_" + ch.lower()
        else:
            result += ch.lower()
    return result
