def convert_to_kgs(lbs):
    kgs = round((lbs * 0.453592), 2)

    pound_word = "pound" if lbs == 1 else "pounds"
    kilogram_word = "kilogram" if kgs == 1 else "kilograms"

    return f"{lbs} {pound_word} equals {kgs:.2f} {kilogram_word}."
