def parse_italics(text: str) -> str:
    result = []
    i = 0
    n = len(text)

    while i < n:
        if text[i] in "*_":
            marker = text[i]
            j = i + 1

            if j < n and text[j] != " ":
                while j < n and text[j] != marker:
                    j += 1

                if j < n and text[j - 1] != " ":
                    result.append("<i>" + text[i + 1:j] + "</i>")
                    i = j + 1
                    continue

        result.append(text[i])
        i += 1

    return "".join(result)
