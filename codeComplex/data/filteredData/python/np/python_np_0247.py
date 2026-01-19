import math

def main(n):
    # Deterministically construct parameters based on n
    if n < 3:
        n = 3
    max_n = 12
    if n > max_n:
        n = max_n
    num_nodes = n
    m = max(1, num_nodes // 2)
    k = num_nodes * num_nodes

    # Generate a deterministic list of floats a of length n
    a = [float((i * 3 + 1) % 10) for i in range(num_nodes)]

    # Generate deterministic tree matrix data: fully filled with a pattern
    tree = [[0.0] * num_nodes for _ in range(num_nodes)]
    cnt = 0
    for i in range(num_nodes):
        for j in range(num_nodes):
            if cnt < k:
                # z derived deterministically from i, j
                z = (i * num_nodes + j + 1) % 7
                tree[i][j] = float(z)
                cnt += 1

    # Original algorithm logic starts here, adapted to use generated data
    po = [1]
    while len(po) != num_nodes:
        po.append(po[-1] * 2)
    dp = [[0.0] * (po[-1] * 2) for _ in range(num_nodes)]
    for i in range(num_nodes):
        dp[i][po[i]] = a[i]
    for mask in range(po[-1] * 2):
        for j in range(num_nodes):
            if mask & po[j]:
                base = dp[j][mask]
                if base == 0.0 and mask != po[j]:
                    continue
                for k_idx in range(num_nodes):
                    if not (mask & po[k_idx]):
                        new_mask = mask + po[k_idx]
                        val = base + a[k_idx] + tree[j][k_idx]
                        if val > dp[k_idx][new_mask]:
                            dp[k_idx][new_mask] = val
    ma = 0.0
    for mask in range(po[-1] * 2):
        if bin(mask)[2:].count("1") == m:
            for j in range(num_nodes):
                if dp[j][mask] > ma:
                    ma = dp[j][mask]
    result = int(ma)
    print(result)
    return result

if __name__ == "__main__":
    main(10)