def count_medals(winners):
    medals = {}  # country -> [gold, silver, bronze]

    # Count medals
    for gold, silver, bronze in winners:
        if gold not in medals:
            medals[gold] = [0, 0, 0]
        if silver not in medals:
            medals[silver] = [0, 0, 0]
        if bronze not in medals:
            medals[bronze] = [0, 0, 0]

        medals[gold][0] += 1
        medals[silver][1] += 1
        medals[bronze][2] += 1

    # Convert to sortable list
    rows = []
    for country in medals:
        g, s, b = medals[country]
        total = g + s + b
        rows.append((country, g, s, b, total))

    # Sort: gold desc, name asc
    rows.sort(key=lambda x: (-x[1], x[0]))

    # Build CSV
    result = "Country,Gold,Silver,Bronze,Total"
    for country, g, s, b, total in rows:
        result += "\n" + country + "," + str(g) + "," + str(s) + "," + str(b) + "," + str(total)

    return result
