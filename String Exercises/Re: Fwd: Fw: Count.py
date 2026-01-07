def email_chain_count(subject):
    subject = subject.lower()

    count= 0
    i= 0
    s= len(subject)
    while i<s:
        if subject.startswith("fw:",i):
            count+=1
            i+=3
        elif subject.startswith("fwd:",i):
            count+=1
            i+=4
        elif subject.startswith("re:",i):
            count+=1
            i+=3
        else:
            i+=1
    return count
