def main(n):
    from math import log
    from collections import deque

    # Deterministic generation of k and s based on n
    # k grows with n but stays non-trivial
    k = max(2, n // 3 + 7)

    # Generate n positive integers with varying digit lengths
    # Values are deterministic functions of i and k
    s = []
    for i in range(1, n + 1):
        base = i * 123457 % (10 ** 9 + 7)
        val = (base * (i % 10 + 1) + k * (i // 2 + 1)) % 10**10 + 1
        s.append(val)

    ans = 0
    s.sort()
    s1 = deque(s)
    for j in range(11):
        d = dict()
        z = 10**j
        for i in s:
            y = i * z
            u = y % k
            if u in d:
                d[u] += 1

            else:
                d[u] = 1
        aux = 0
        for i in s1:
            y = i
            lg = int(log(i, 10)) + 1
            lg = 10**lg
            if lg == z:
                key = (y * z) % k
                d[key] -= 1
                x = (k - y % k)
                if y % k == 0:
                    x = 0
                if x in d:
                    ans += d[x]
                d[key] += 1
                aux += 1

            else:
                break
        for _ in range(aux):
            s1.popleft()

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)