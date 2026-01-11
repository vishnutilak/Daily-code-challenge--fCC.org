def has_consonant_count(text, target):
    consonants = set("bcdfghjklmnpqrstvwxyz")
    count =0
    for ch in text:
        if ch.isalpha() and ch.lower() in consonants:
                count+=1

    return count==target
