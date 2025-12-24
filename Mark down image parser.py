def parse_image(markdown):
    alt_start = markdown.find("![") + 2
    alt_end = markdown.find("]")
    url_start = markdown.find("(") + 1
    url_end = markdown.find(")")

    alt_text = markdown[alt_start:alt_end]
    image_url = markdown[url_start:url_end]

    return f'<img src="{image_url}" alt="{alt_text}">'
