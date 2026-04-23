def get_cleanup_score(items):
    values = {
        "bottle": 10, "can": 6, "bag": 8, "tire": 35,
        "straw": 4, "cardboard": 3, "newspaper": 3,
        "shoe": 12, "electronics": 25, "battery": 18, "mattress": 38
    }

    total =0
    prev_item = None
    streak =0

    for i in range(len(items)):
        item = items[i]

        if isinstance(item, list) and item[0]=="rare":
            curr_value = item[1]
            prev_item =None
            streak =0
        else:
            base_val = values[item]

            if item== prev_item:
                streak +=1
            else:
                streak=0
            curr_value = base_val +streak
            prev_item =item

            #multiplier here
            if (i+1)%5==0:

                curr_value *=((i+1)//5)+1
        
        total+=curr_value
    
    return total
##that took longer than expected to solve
