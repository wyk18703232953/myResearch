def Solve(n):
    if n <=2:
        return n
    elif n % 6== 0:
        return (n -1)*(n -2)*(n - 3)
    elif n % 2 == 0:
        return n * (n - 1) * (n - 3)
    else:
        return n * (n - 1) * (n - 2)

n = int(input())
print(Solve(n))