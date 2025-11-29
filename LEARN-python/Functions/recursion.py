def recursion(n):
    if n == 0:
        return 0
    else:
        return n + recursion(n-1)
sum=recursion(5)
print(sum)