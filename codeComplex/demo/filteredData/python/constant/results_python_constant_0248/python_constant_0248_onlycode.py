n, m = int(input()), int(input())
print(m % (2 ** n) if n < 30 else m)