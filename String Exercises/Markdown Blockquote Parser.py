def parse_blockquote(markdown):
    i = 0
    n = len(markdown)

    # Skip leading spaces
    while i < n and (markdown[i] == ' ' or not markdown[i].isalnum()):
        i += 1

    item_text = markdown[i:]

    return "<blockquote>" + item_text + "</blockquote>"
