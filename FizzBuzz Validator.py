def is_fizz_buzz(arr):
    for i, val in enumerate(arr):
        if isinstance(val, int):
            start = val-i
            break
            ##to pick an anchor to start
    else:
        return False
        
    for i, val in enumerate(arr):
        num = start+i

        if num%15==0:
            expected ="FizzBuzz"
        elif num%3==0:
            expected ="Fizz"
        elif num%5==0:
            expected ="Buzz"
        else:
            expected = num
        
        if val!= expected:
            return False
    return True
