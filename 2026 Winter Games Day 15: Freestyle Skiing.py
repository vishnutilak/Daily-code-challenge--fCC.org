def is_valid_trick(trick_name):
    tricks = trick_name.split(" ")
    first_words = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
    second_words = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]

    if tricks[0] in first_words and tricks[1] in second_words:
        return True
    else:
        return False
