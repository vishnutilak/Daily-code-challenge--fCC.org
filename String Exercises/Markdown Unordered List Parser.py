def parse_unordered_list(markdown):
    lines = markdown.split("\n")
    items = []

    for line in lines:
        # remove leading "-" and surrounding whitespace
        text = line[1:].strip()
        items.append(f"<li>{text}</li>")

    return "<ul>" + "".join(items) + "</ul>"
