def can_donate(donor, recipient):
    donor_type = donor[:-1]
    donor_rh = donor[-1]

    recipient_type = recipient[:-1]
    recipient_rh = recipient[-1]


    #AOB compatibility
    don_chart = {
        "O":{"A", "B", "AB", "O"},
        "A":{"A","AB"},
        "B":{"B", "AB"},
        "AB":{"AB"}}
    
    if recipient_type not in don_chart[donor_type]:
        return False
    if recipient_rh=="-" and donor_rh=="+":
        return False
    
    return True
