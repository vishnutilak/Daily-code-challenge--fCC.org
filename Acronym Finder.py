def find_org(acronym):
    orgs = {"NASA":"National Avocado Storage Authority",
    "CIA":"Cats Infiltration Agency",
    "FBI":"Fluffy Beanbag Inspectors",
    "DOJ":"Department Of Jelly",
    "WHO":"Wild Honey Organization",
    "EPA":"Eating Pancakes Administration"}

    return orgs.get(acronym)

# def find_org(abbreviation):
#     words = abbreviation.split(" ")
#     res =[]
#     for word in words:
#         res.append(word[0])
#     return "".join(res)
