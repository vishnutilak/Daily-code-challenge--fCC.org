def convert_to_km(miles):
    km = miles * 1.60934

    result = f"{km:.2f}"
    result = result.rstrip('0').rstrip('.')

    return float(result) if result else 0
