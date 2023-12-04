def fuumo(x,n):
    if n==0:
        return 1.0 + 0.0*x
    elif n==1:
        return 2.0*x
    else:
        return 2.0*x*fuumo(x,n-1) - 2.0*(n-1)*fuumo(x,n-2)

print(fuumo(3,4))