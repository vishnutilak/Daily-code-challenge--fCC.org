def format_date(date_string):
    month_map = {
        "January": "01", "February": "02", "March": "03",
        "April": "04", "May": "05", "June": "06",
        "July": "07", "August": "08", "September": "09",
        "October": "10", "November": "11", "December": "12"
    }

    parts = date_string.split()
    month = month_map[parts[0]]
    day = parts[1][:-1]      # remove comma
    year = parts[2]

    if len(day) == 1:
        day = "0" + day

    return year + "-" + month + "-" + day
