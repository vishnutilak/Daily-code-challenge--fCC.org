def add_punctuation(s):

    result = []

    for i in range(len(s)):
        result.append(s[i])

        if s[i] == " " and i + 1 < len(s) and s[i + 1].isupper():
            result.insert(len(result) - 1,".")

    if not result or result[-1] != ".":
        result.append(".")

    return "".join(result)
