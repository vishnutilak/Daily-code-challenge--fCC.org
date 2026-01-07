def resolution_streak(days):
    streak = 0

    for i, (steps, screen, pages) in enumerate(days, start=1):
        if steps >= 10000 and screen <= 120 and pages >= 5:
            streak += 1
        else:
            return f"Resolution failed on day {i}: {streak} day streak."

    return f"Resolution on track: {streak} day streak."
