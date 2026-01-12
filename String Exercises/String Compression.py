def compress_string(sentence):
    words =sentence.split()
    result =[]
    prev = words[0]
    count =1

    for i in range(1,len(words)):
        if words[i] == prev:
            count += 1

        else:
            if count > 1:
                result.append(f"{prev}({count})")
            else:
                result.append(prev)
            
            prev = words[i]
            count = 1

    # flush last word
    if count > 1:
        result.append(f"{prev}({count})")
    else:
        result.append(prev)

    return " ".join(result)
