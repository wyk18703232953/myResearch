n = int(input()) + 1
if n == 1:
    print(0)
    exit()
print(n if n % 2 else n // 2)
