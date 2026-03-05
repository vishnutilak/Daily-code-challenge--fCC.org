def count_perfect_cubes(a, b):
    low= min(a,b)
    high= max(a,b)

    def get_cubic_root(x):
        if x<0:
            return -round(abs(x)**(1/3))
        return round(x**(1/3))
    
    start_root = get_cubic_root(low)
    end_root = get_cubic_root(high)

    if start_root**3<low:
        start_root +=1
    if end_root**3 >high:
        end_root -=1
    
    return end_root-start_root+1
