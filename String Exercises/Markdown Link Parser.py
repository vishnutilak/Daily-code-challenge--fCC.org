def parse_link(markdown):
    open_brack = markdown.find('[')
    close_brack = markdown.find(']')
    open_paran = markdown.find('(')
    close_paran = markdown.find(')')

    link_text = markdown[open_brack+1: close_brack]
    link_url =markdown[open_paran+1: close_paran]

    return '<a href="'+ link_url+'">'+link_text+'</a>'
