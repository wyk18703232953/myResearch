def main(n):
    # Interpret n as the array length; choose m deterministically based on n
    # Ensure m >= 1 and reasonably related to n
    m = max(1, n // 3 + 1)

    # Deterministic construction of arr of length n
    # Example pattern: arr[i] = (i * 7 + 3) % (5 * m) + i // 2
    arr = [((i * 7 + 3) % (5 * m)) + (i // 2) for i in range(n)]

    from collections import deque

    mods = [0 for _ in range(m)]
    placement = [[] for _ in range(m)]

    for i in range(n):
        r = arr[i] % m
        mods[r] += 1
        placement[r].append(i)

    cnt = 0
    queue = deque()
    target = n // m

    for i in range(2 * m):
        mod = i % m
        if mods[mod] > target:
            excess = mods[mod] - target
            for c in range(excess):
                queue.append([i, placement[mod][c]])
            mods[mod] = target
        elif mods[mod] < target:
            while queue and mods[mod] < target:
                elem, idx = queue.popleft()
                delta = (mod - elem) % m
                mods[mod] += 1
                cnt += delta
                arr[idx] += delta

    # print(cnt)
    pass
    # print(' '.join(str(x) for x in arr))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)