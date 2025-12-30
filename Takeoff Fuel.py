import math
def fuel_to_add(current_gallons, required_liters):

    required_gallons = required_liters/3.78541
    if current_gallons >= required_gallons:
        return 0
    else:
        return math.ceil(required_gallons- current_gallons)
