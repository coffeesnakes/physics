def search(arr, lo, hi, n):
    while lo <= hi:
        m = (lo+(hi-lo)//2)
        v = arr[m]
        if v == n:
            return True
        elif v > n:
            lo = m+1
        else:
            hi = m-1
    return False