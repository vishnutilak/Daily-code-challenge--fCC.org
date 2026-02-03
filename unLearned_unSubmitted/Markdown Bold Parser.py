def parse_bold(text: str) -> str:
    result = []
    i = 0
    n = len(text)

    while i < n:
        # Check for opening bold marker
        if i + 1 < n and text[i:i+2] in ("**", "__"):
            marker = text[i:i+2]
            start = i + 2

            # No space allowed right after opening
            if start < n and text[start] != " ":
                j = start

                # Search for closing marker
                while j + 1 < n and text[j:j+2] != marker:
                    j += 1

                # Found closing marker, validate no space before it
                if j + 1 < n and text[j - 1] != " ":
                    result.append("<b>" + text[start:j] + "</b>")
                    i = j + 2
                    continue

        # Default: copy character
        result.append(text[i])
        i += 1

    return "".join(result)
