def main(n):
    from math import log
    from collections import deque

    # Deterministic data generation:
    # Map n to:
    #   k: a fixed positive integer > 1
    #   s: list of length n with positive integers
    # Ensure values are reasonable and exercise the algorithm.
    if n <= 0:
        print(0)
        return

    k = 10**9 + 7  # large prime, fixed

    # Generate s deterministically: mix of values with different digit lengths
    s = []
    for i in range(1, n + 1):
        # Construct numbers with varying magnitudes and patterns
        # This is fully deterministic and only depends on n and i
        base = i * 123457 % (10**9)
        val = base + (10**(i % 9))  # ensure at least one significant digit position varies
        s.append(val)

    ans = 0
    s.sort()
    s1 = deque(s)
    for j in range(11):
        d = dict()
        z = 10 ** j
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
            lg = 10 ** lg
            if lg == z:
                aux1 = (y * z) % k
                aux2 = y % k
                d[aux1] -= 1
                x = (k - aux2)
                if aux2 == 0:
                    x = 0
                if x in d:
                    ans += d[x]
                d[aux1] += 1
                aux += 1
            else:
                break
        for _ in range(aux):
            s1.popleft()
    print(ans)


if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(1000)