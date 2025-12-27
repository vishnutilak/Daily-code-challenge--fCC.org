def generate_snowflake(crystals):

    lines = crystals.split('\n')
    mirrored_lines =[]

    for line in lines:
        mirrored_lines.append(line+ line[::-1])
    
    return '\n'.join(mirrored_lines)
