def truncate_text(text):
    return text[:17]+"..." if len(text)>20 else text
