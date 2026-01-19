def compare_energy(calories_burned, watt_hours_used):
    energy_spent = calories_burned *4184

    watts_spent = watt_hours_used *3600

    if energy_spent > watts_spent:
        return "Workout"
    if watts_spent > energy_spent:
        return "Devices"
    else:
        return "Equal"
