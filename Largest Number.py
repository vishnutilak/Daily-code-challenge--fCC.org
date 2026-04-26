def largest_number(s):
    nums =[]
    curr=""

    for ch in s:
        if ch.isdigit() or ch in '.-':
            curr+=ch
        else:
            if curr:
                nums.append(float(curr))
                curr = ""
    if curr:
        nums.append(float(curr))
    
    result = max(nums)

    return int(result) if result.is_integer() else result
