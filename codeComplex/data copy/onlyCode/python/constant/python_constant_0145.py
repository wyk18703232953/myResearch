def prime(n):
    if n < 2:
        return False
    elif n % 2 == 0 and n != 2:
        return False
    for j in range(3, int(pow(n, 0.5) + 1), 2):
        if n % j == 0:
            return False
    return True
n = int(input())
for j in range(2, int(n / 2) + 1):
    if prime(j) == False and prime(n - j) == False:
        print(j, n - j)
        break
