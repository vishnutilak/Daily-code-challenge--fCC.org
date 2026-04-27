def sum_letters(s):
    total =0
    for ch in s:
        if ch.isalpha():
            total += ord(ch.lower())-ord('a') + 1
    
    return total

def get_word_score(word):

    total =0
    for ch in word:
        if ch.isalpha():
            total += ord(ch.lower())-ord('a') + 1
    
    return total
