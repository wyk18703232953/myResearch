def main(n):
    # Deterministic data generation: degree list a[1..n]
    # Example: ensure sum(a) >= 2*(n-1) is not enforced; we just mimic original behavior.
    # Pattern: a[i] cycles through [0,1,2,3] for variety.
    a = [0]
    total_sum = 0
    for i in range(1, n + 1):
        val = i % 4  # 0,1,2,3 pattern
        a.append(val)
        total_sum += val

    edge = []
    last = 0
    ans = 0

    # Find last position with a[i] == 1
    for i in range(1, n + 1):
        if a[i] == 1:
            last = i
    if last != 0:
        a[last] = 0

    # Connect nodes with degree > 1
    for i in range(1, n + 1):
        if a[i] > 1:
            if last:
                edge.append([last, i])
                ans += 1
            last = i

    # Connect remaining degree-1 nodes to last
    for i in range(1, n + 1):
        if a[i] == 1 and last:
            edge.append([last, i])
            last = 0
            a[i] = 0
            ans += 1

    # Try to connect remaining degree-1 nodes using nodes with degree > 2
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[j] == 1 and a[i] > 2:
                edge.append([i, j])
                a[i] -= 1
                a[j] -= 1

    if len(edge) != n - 1:
        # print("NO")
        pass

    else:
        # print("YES", ans)
        pass
        # print(len(edge))
        pass
        for u, v in edge:
            # print(u, v)
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)