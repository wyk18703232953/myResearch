def main(n):
    import heapq  # kept as in original, though unused in logic

    # Generate key list as in original code
    key = []
    for i in ['S', 'M', 'L']:
        for j in range(4):
            key.append(j * 'X' + i)

    # Initialize dictionaries
    prev = dict().fromkeys(key, 0)
    now = dict().fromkeys(key, 0)

    # Deterministically generate "prev" multiset of sizes based on n
    # Distribute counts across key patterns in a fixed cyclic manner
    for i in range(n):
        size = key[i % len(key)]
        prev[size] += 1

    # Deterministically generate "now" multiset of sizes based on n
    # Use a shifted pattern to create differences
    for i in range(n):
        size = key[(i * 2) % len(key)]
        now[size] += 1

    # Core logic: cancel matching sizes
    for k in key:
        temp = min(prev[k], now[k])
        prev[k] -= temp
        now[k] -= temp

    ans = 0
    for k in key:
        ans += now[k]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)