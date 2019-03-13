def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <= will stop once you have reached the smaller number, 
                           # which means target is smaller than any
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:  # will stop once you've reached the higher number, which means the target is larger than any
                break       
            lower = x
        elif target < val:
            upper = x
