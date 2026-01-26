def main(n):
    # Deterministic data generation:
    # Generate n pairs (k, m) where k is increasing and m is a small periodic value
    # This keeps structure similar to arbitrary input while being fully deterministic.
    l = [(i * 3, (i % 5) + 1) for i in range(n)]

    # Core logic from original program
    l.sort(key=lambda x: x[0] + x[1])

    if n == 0:
        # print(0)
        pass
        return

    last = 0
    ans = 1

    for i in range(1, n):
        if abs(l[i][0] - l[last][0]) >= l[i][1] + l[last][1]:
            last = i
            ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)