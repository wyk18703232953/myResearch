import sys

def is_prime(x):
    return all(x%i for i in range(2, int(x**.5)+1))

t = int(sys.stdin.read().strip())
for i in range(4, t//2+1):
    if not is_prime(i) and not is_prime(t-i):
        print(i, t-i, sep=' ')
        break
