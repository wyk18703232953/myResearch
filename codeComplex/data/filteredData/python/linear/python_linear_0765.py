import collections
import math

mod = (10 ** 9) + 7

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def isprime(x):
    if x == 1:
        return False
    elif x < 4:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def main(n):
    if n < 2:
        n = 2
    # Deterministic mapping from n to problem parameters
    N = n
    Q = n

    # Generate array a of length N deterministically
    # Ensure there is a clear maximum; let the last element be the maximum
    a = [(i * 2 + 3) for i in range(N - 1)]
    g = max(a) + 5
    a.append(g)

    d = collections.deque(a)
    f = 0
    an1 = []
    while d[0] != g:
        f += 1
        x = d.popleft()
        y = d.popleft()
        an1.append(str(x) + " " + str(y))
        if y == g:
            d.appendleft(y)
            d.append(x)
            break
        if x < y:
            d.appendleft(y)
            d.append(x)
        else:
            d.appendleft(x)
            d.append(y)
    r = []
    ans = []
    for _ in range(N):
        r.append(str(d.popleft()))

    # Generate Q deterministic queries
    queries = [i + 1 for i in range(Q)]

    for b in queries:
        if b <= f:
            ans.append(an1[b - 1])
        else:
            b -= f
            b -= 1
            b %= (N - 1)
            ans.append(r[0] + " " + r[b + 1])
    print("\n".join(ans))

if __name__ == "__main__":
    main(10)