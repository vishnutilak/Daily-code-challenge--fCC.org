def insert_into_array(arr, value, index):
    arr_head = arr[:index]
    # arr_tail = arr[index:]

    arr_head.append(value)
    arr_head.extend(arr[index:])

    return arr_head
