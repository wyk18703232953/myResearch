import random

def matches(pos, c, case):
    if case == 0:
        return pos % 3 == "RGB".index(c)
    elif case == 1:
        return pos % 3 == "GBR".index(c)
    else:
        return pos % 3 == "BRG".index(c)

def solve_one(n, k, s):
    mglobal = k
    r = g = b = 0

    # initial window [0, k)
    for i, c in enumerate(s[:k]):
        r += not matches(i, c, 0)
        g += not matches(i, c, 1)
        b += not matches(i, c, 2)

    mglobal = min(mglobal, r, g, b)

    # slide window
    for i, c in enumerate(s[k:], start=k):
        # leaving index i-k, entering index i
        r += -(not matches(i - k, s[i - k], 0)) + (not matches(i, c, 0))
        g += -(not matches(i - k, s[i - k], 1)) + (not matches(i, c, 1))
        b += -(not matches(i - k, s[i - k], 2)) + (not matches(i, c, 2))
        mglobal = min(mglobal, r, g, b)

    return mglobal

def main(n):
    """
    n: problem scale, interpreted here as:
       - number of test cases q = n
       - for each test: random length L in [1, n], random k in [1, L]
    """
    random.seed(0)

    q = n
    results = []
    for _ in range(q):
        L = random.randint(1, n)
        k = random.randint(1, L)
        s = ''.join(random.choice('RGB') for _ in range(L))
        ans = solve_one(L, k, s)
        results.append(ans)

    # Output one result per line (like original multiple test cases)
    for x in results:
        print(x)

if __name__ == "__main__":
    main(5)