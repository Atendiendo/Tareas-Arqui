def ncsr(n, k):
    if k > n:
        return 0
    elif n == 1 or k == 0:
        return 1
    else:
        return ncsr(n-1, k) + ncsr(n-1, k-1)
    
print(ncsr(6,3))