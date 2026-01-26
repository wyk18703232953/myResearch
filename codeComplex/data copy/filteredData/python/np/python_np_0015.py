def count_bits(n):
    value = 0
    while n:
        n &= (n - 1)
        value += 1
    return value

def nc2(n):
    return (n * (n - 1)) // 2

def answer(n, a):
    dp = [0.0] * (1 << n)
    dp[(1 << n) - 1] = 1.0  # initially all alive

    for mask in range((1 << n) - 1, 0, -1):
        m = count_bits(mask)
        if m == 1:
            continue

        p = 1.0 / nc2(m)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if (mask >> i) & 1 and (mask >> j) & 1:
                    next_mask = mask ^ (1 << j)
                    dp[next_mask] += dp[mask] * p * a[i][j]

    res = []
    for i in range(n):
        res.append(dp[1 << i])
    return res

def generate_matrix(n):
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0.0)
            else:
                # simple deterministic pattern: (i+1)/(i+j+2)
                row.append((i + 1.0) / (i + j + 2.0))
        a.append(row)
    return a

def main(n):
    a = generate_matrix(n)
    res = answer(n, a)
    for v in res:
        print(v, end=' ')
    print()

if __name__ == "__main__":
    main(3)