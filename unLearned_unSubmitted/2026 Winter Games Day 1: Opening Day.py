def get_flag(code):
    return chr(ord(code[0]) - ord('A') + 0x1F1E6) + \
           chr(ord(code[1]) - ord('A') + 0x1F1E6)
