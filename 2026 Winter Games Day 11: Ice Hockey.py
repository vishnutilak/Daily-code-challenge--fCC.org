def get_semifinal_matchups(teams):
    standings =[]

    for entry in teams:
        parts = entry.split(': ')
        name = parts[0]

        scores = parts[1].split('-')
        W= int(scores[0])
        OTW= int(scores[1])
        OTL= int(scores[2])
        L= int(scores[3])

        points = W*3 + OTW*2 + OTL
        standings.append([name,points])
    
    standings.sort(key= lambda x: x[1], reverse= True)

    first = standings[0][0]
    second = standings[1][0]
    third = standings[2][0]
    fourth = standings[3][0]

    return "The semi-final games will be "+first +" vs " +fourth+ " and "+ second+" vs "+third+"."
