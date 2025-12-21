MOD = 998244353

def power(x, n):
    ans = 1
    while n:
        if n & 1:
            ans = ans * x % MOD
        x = x * x % MOD
        n //= 2
    return ans

def main(n):
    import random
    a = []
    for _ in range(n):
        if random.random() < 0.3:
            a.append(-1)
        else:
            a.append(random.randint(1, n))
    b = [0 for _ in range(n + 1)]
    def add(x, v):
        while x <= n:
            b[x] += v
            x += x & -x
    def get(x):
        ans = 0
        while x:
            ans += b[x]
            x -= x & -x
        return ans
    anss = 0
    for i in range(n):
        if a[i] != -1:
            add(a[i], 1)
            anss += get(n) - get(a[i])
    anss %= MOD
    total = 0
    sur = [0] + [1 for _ in range(n)]
    for i in range(n):
        if a[i] == -1:
            total += 1
        else:
            sur[a[i]] = 0
    if total == 0:
        return anss
    for i in range(1, n + 1):
        sur[i] += sur[i - 1]
    dead = 0
    ansa = 0
    for i in range(n):
        if a[i] != -1:
            ansa += sur[a[i]] * (total - dead) + (sur[n] - sur[a[i]]) * dead
        else:
            dead += 1
    ans = (ansa * 4 + anss * 4 * total + total * total * (total - 1)) % MOD
    ans = ans * power(4 * total, MOD - 2) % MOD
    return ans

if __name__ == "__main__":
    print(main(10))