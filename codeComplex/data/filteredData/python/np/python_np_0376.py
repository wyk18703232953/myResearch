import math

INF = float('inf')

def cord(c):
    return ord(c) - ord('a')

def generate_input(n):
    m = max(1, min(20, n))  # limit m to keep 1<<m manageable
    length = max(2, n)      # ensure at least two characters
    s_chars = []
    for i in range(length):
        # deterministic pattern using i and m
        s_chars.append(chr(ord('a') + (i * 7 + 3) % m))
    s = ''.join(s_chars)
    return length, m, s

def main(n):
    n, m, s = generate_input(n)
    ct = [0] * (1 << m)

    for i in range(n - 1):
        now, nex = cord(s[i]), cord(s[i + 1])
        if now == nex:
            continue
        ct[(1 << now) | (1 << nex)] += 1

    for i in range(m):
        for j in range(1 << m):
            if (1 << i) & j:
                ct[j] += ct[(1 << i) ^ j]

    dp = [INF] * (1 << m)
    dp[0] = 0
    total = ct[(1 << m) - 1]
    full_mask = (1 << m) - 1

    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j) == 0:
                # emulate ct[-1]-ct[i]-ct[~i] from original (with bounded masks)
                complement_mask = (~i) & full_mask
                sm = total - ct[i] - ct[complement_mask]
                ni = i | (1 << j)
                if dp[i] + sm < dp[ni]:
                    dp[ni] = dp[i] + sm

    print(dp[full_mask])

if __name__ == "__main__":
    main(10)