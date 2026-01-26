def main(n):
    # Map n to problem parameters deterministically
    # For scalability, let number of knights = n, and m = n // 2 (at least 1)
    num_knights = n if n > 0 else 1
    m = max(1, num_knights // 2)

    class Knight:
        def __init__(self, andis, p, c):
            self.p = int(p)
            self.c = int(c)
            self.andis = int(andis)
            self.ans = self.c

    # Deterministic generation of p and c based on n
    # p: strictly increasing "power" values
    p = [i * 2 + 1 for i in range(num_knights)]
    # c: coin values with a simple deterministic pattern
    c = [(i * 3 + 7) % (num_knights + 5) + 1 for i in range(num_knights)]

    x = []
    for i in range(num_knights):
        x.append(Knight(i, p[i], c[i]))

    x.sort(key=lambda x: x.p)
    coins = []
    for i in range(num_knights - 1):
        if len(coins) < m:
            coins.append(x[i].c)
            coins.sort()
        elif len(coins) > 0:
            if coins[0] < x[i].c:
                coins[0] = x[i].c
                coins.sort()
        x[i + 1].ans += sum(coins)

    x.sort(key=lambda x: x.andis)
    output = []
    for k in x:
        output.append(str(k.ans))
    # print(" ".join(output))
    pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)