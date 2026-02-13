def get_relative_results(results):
    def to_seconds(t):
        parts = t.split(":")
        hh = int(parts[0])
        mm = int(parts[1])
        ss = int(parts[2])

        return (hh*3600)+(mm*60)+ss
    winner_time = to_seconds(results[0])
    result = ["0"]
    for i in range(1, len(results)):
        diff = to_seconds(results[i]) - winner_time
        minutes = diff // 60
        seconds = diff % 60
        if seconds < 10:
            result.append("+" + str(minutes) + ":0" + str(seconds))
        else:
            result.append("+" + str(minutes) + ":" + str(seconds))

    return result
