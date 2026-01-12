def get_number_of_plants(field_size, unit, crop):
    crop_map ={"corn": 1, "wheat":0.1, "soybeans": 0.5, "tomatoes": 0.25, "lettuce":0.2}

    if unit =="hectares":
        landMtrs = field_size * 10000
    else: #acres
        landMtrs = field_size * 4046.86
    

    plants = landMtrs / crop_map[crop]

    return int(plants)
