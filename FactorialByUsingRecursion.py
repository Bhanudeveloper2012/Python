def fact(n):
    if n ==1 or n==0:
        return n
    else:
        return n*fact(n-1)

ans=fact(3)
print(ans)

