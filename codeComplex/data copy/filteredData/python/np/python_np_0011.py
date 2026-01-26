import math

def count_bits(x, n):
    cnt = 0
    for i in range(n):
        if (1 << i) & x:
            cnt += 1
    return cnt

def main(n):
    if n <= 0:
        return

    # Deterministically generate an n x n matrix a of floats in [0,1),
    # with zero diagonal and each row summing to 1 when possible.
    a = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        row_sum = 0.0
        for j in range(n):
            if i == j:
                a[i][j] = 0.0
            else:
                # Simple deterministic pattern based on i, j
                val = ((i + 1) * (j + 1)) % (n + 1)
                a[i][j] = float(val)
                row_sum += a[i][j]
        if row_sum > 0:
            for j in range(n):
                a[i][j] = a[i][j] / row_sum
        else:
            # Fallback if row_sum == 0, distribute uniformly on off-diagonal
            for j in range(n):
                if i != j:
                    a[i][j] = 1.0 / (n - 1) if n > 1 else 0.0
                else:
                    a[i][j] = 0.0

    dp = [0.0 for _ in range(1 << n)]
    dp[-1] = 1.0

    for mask in range((1 << n) - 1, -1, -1):
        val = count_bits(mask, n)
        if val < 2:
            continue
        total = val * (val - 1) // 2
        for i in range(n):
            if (mask & (1 << i)) == 0:
                continue
            for j in range(n):
                if (mask & (1 << j)) == 0 or i == j:
                    continue
                dp[mask ^ (1 << j)] += dp[mask] * a[i][j] / total

    for i in range(n):
        print(dp[1 << i])

if __name__ == "__main__":
    main(4)