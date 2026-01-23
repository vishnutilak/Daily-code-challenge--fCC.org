def get_average_grade(scores):
    avg = sum(scores) / len(scores)

    if avg >= 97:
        return "A+"
    elif avg >= 93:
        return "A"
    elif avg >= 90:
        return "A-"
    elif avg >= 87:
        return "B+"
    elif avg >= 83:
        return "B"
    elif avg >= 80:
        return "B-"
    elif avg >= 77:
        return "C+"
    elif avg >= 73:
        return "C"
    elif avg >= 70:
        return "C-"
    elif avg >= 67:
        return "D+"
    elif avg >= 63:
        return "D"
    elif avg >= 60:
        return "D-"
    else:
        return "F"
