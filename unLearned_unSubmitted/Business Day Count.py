
def count_business_days(start_date, end_date):

    # ---------- helper: parse "YYYY-MM-DD" ----------
    def parse(date_str):
        parts = date_str.split("-")
        y = int(parts[0])
        m = int(parts[1])
        d = int(parts[2])
        return y, m, d

    # ---------- helper: check leap year ----------
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # ---------- helper: days in month ----------
    def days_in_month(year, month):
        if month == 2:
            return 29 if is_leap(year) else 28
        if month in (4, 6, 9, 11):
            return 30
        return 31

    # ---------- helper: convert date to day number ----------
    # counts total days from 0001-01-01
    def to_ordinal(y, m, d):
        days = 0

        # add days from previous years
        for year in range(1, y):
            days += 366 if is_leap(year) else 365

        # add days from previous months
        for month in range(1, m):
            days += days_in_month(y, month)

        # add days in current month
        days += d

        return days

    # ---------- helper: weekday ----------
    # 0001-01-01 was a Monday
    # Monday=0 ... Sunday=6
    def weekday(y, m, d):
        return (to_ordinal(y, m, d) - 1) % 7

    # ---------- main logic ----------
    sy, sm, sd = parse(start_date)
    ey, em, ed = parse(end_date)

    count = 0

    y, m, d = sy, sm, sd

    while True:
        wd = weekday(y, m, d)
        if wd < 5:   # 0–4 → Monday–Friday
            count += 1

        if (y, m, d) == (ey, em, ed):
            break

        # move to next day
        d += 1
        if d > days_in_month(y, m):
            d = 1
            m += 1
            if m > 12:
                m = 1
                y += 1

    return count
