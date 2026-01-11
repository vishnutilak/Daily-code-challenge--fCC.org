def update_inventory(inventory, shipment):

    index ={}
    for i in range(len(inventory)):
        item = inventory[i][1]
        index[item] =i

    for qty, item in shipment:
        if item in index:
            inventory[index[item]][0] += qty
        else:
            inventory.append([qty,item])
            index[item] = len(inventory)-1

    return inventory
