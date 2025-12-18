def Is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
for i in range(2, 100):
    if not Is_prime(i) and not Is_prime(n - i):
        print(i, n - i)
        break
# print(Is_prime(n))
