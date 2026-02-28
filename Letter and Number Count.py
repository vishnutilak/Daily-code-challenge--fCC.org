def count_letters_and_numbers(s):
    letters = 0
    numbers = 0

    for ch in s:
        if ch.isalpha():
            letters+=1
        if ch.isdigit():
            numbers +=1
    
    letter_word = "letter" if letters==1 else "letters"
    number_word = "number" if numbers==1 else "numbers"

    return f"The string has {letters} {letter_word} and {numbers} {number_word}."
