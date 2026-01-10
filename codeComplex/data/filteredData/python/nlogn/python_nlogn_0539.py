def main(n):
    from math import log

    # Deterministic generation of k and s based on n
    if n <= 0:
        return 0

    k = n * 2 + 1  # k grows with n, always odd and > 0

    # Generate n positive integers with varying digit lengths
    # Example pattern: values around powers of 10 to exercise log10 behavior
    s = []
    base = 1
    for i in range(n):
        # Change base every time i hits a power of 2 to get different magnitudes
        if i > 0 and (i & (i - 1)) == 0:
            base *= 10
        s.append(base + i)

    ans = 0
    for j in range(11):
        d = {}
        z = 10 ** j
        for i in s:
            y = i * z
            u = y % k
            if u in d:
                d[u] += 1
            else:
                d[u] = 1
        for i in s:
            y = i
            lg = int(log(i, 10)) + 1
            lg = 10 ** lg
            if lg == z:
                idx = (y * z) % k
                d[idx] -= 1
                x = (k - y % k)
                if y % k == 0:
                    x = 0
                if x in d:
                    ans += d[x]
                d[idx] += 1
    return ans


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(1000)
    print(result)