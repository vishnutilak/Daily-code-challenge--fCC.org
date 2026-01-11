def has_consonant_count(text, target):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count =0
    for ch in text:
        if ch.isalpha():
            if ch.lower() in consonants:
                count+=1

    return count==target
