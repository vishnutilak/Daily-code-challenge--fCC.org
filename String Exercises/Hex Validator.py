def is_valid_hex(s):
    if s[0]!= '#' or not s:
        return False

    if len(s)!=4 and len(s)!=7:
        return False

    hex_chars ="abcdef1234567890ABCDEF"

    for ch in s[1:]:
        if ch not in hex_chars:
            return False
    return True
