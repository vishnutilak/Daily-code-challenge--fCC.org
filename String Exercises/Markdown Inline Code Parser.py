def parse_inline_code(markdown):
    result = []
    in_code = False

    for ch in markdown:
        if ch == '`':
            if not in_code:
                result.append('<code>')
            else:
                result.append('</code>')
            in_code = not in_code
        else:
            result.append(ch)

    return ''.join(result)
