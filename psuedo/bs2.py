def bs (arr,lo, hi, t):
    while lo <= hi:
        m = (lo + (hi-lo))//2
        v = arr[m]
        if v == t:
            return True
        if v > t:
            lo = m + 1
        elif v < t:
            hi = m - 1
        
    return False