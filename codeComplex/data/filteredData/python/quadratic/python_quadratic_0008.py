import math

def main(n):
    # n is the number of points
    if n <= 0:
        return

    # Deterministic generation of x: simple arithmetic progression
    x = [i for i in range(n)]

    # Deterministic radius depending on n, but fixed for given n
    # Ensure r >= 1
    r = max(1, n // 2)

    ans = []
    for i in range(n):
        t = r
        for j in range(i):
            a = abs(x[i] - x[j])
            if a <= 2 * r:
                t2 = (2 * r) ** 2
                t2 -= a ** 2
                t2 = math.sqrt(t2) + ans[j]
                t = max(t, t2)
        ans.append(t)
    for k in ans:
        print(k)


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)