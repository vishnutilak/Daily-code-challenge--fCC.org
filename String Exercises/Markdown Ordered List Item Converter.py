def convert_list_item(s):
    i = 0
    n = len(s)

    # Skip leading spaces
    while i < n and s[i] == ' ':
        i += 1

    # Must start with a digit
    if i >= n or not s[i].isdigit():
        return "Invalid format"

    # Read the number
    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    # Number must be >= 1
    if num < 1:
        return "Invalid format"

    # Next must be a period immediately
    if i >= n or s[i] != '.':
        return "Invalid format"

    i += 1

    # Must have at least one space after the period
    if i >= n or s[i] != ' ':
        return "Invalid format"

    # Skip spaces after period
    while i < n and s[i] == ' ':
        i += 1

    # Must have text remaining
    if i >= n:
        return "Invalid format"

    item_text = s[i:]

    return "<li>" + item_text + "</li>"
