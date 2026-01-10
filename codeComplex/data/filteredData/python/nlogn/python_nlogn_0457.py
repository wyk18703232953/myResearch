def main(n):
    import heapq

    if n <= 0:
        return

    # Define k as a function of n, at least 1 and at most n
    k = max(1, min(n, n // 3 if n >= 3 else 1))

    # Deterministically generate arr of length n
    # Example pattern: arr[i] = (i * 7 + 3) % 1000 + 1
    arr = [(i * 7 + 3) % 1000 + 1 for i in range(n)]

    q = []
    for i in range(n):
        heapq.heappush(q, (-arr[i], i))

    res = []
    temp_k = k
    while temp_k:
        val, idx = heapq.heappop(q)
        res.append((-val, idx))
        temp_k -= 1

    res.sort(key=lambda x: x[1])

    ans = 0
    for v, _ in res:
        ans += v

    path = []
    cnt = 0
    for i in range(n):
        if (arr[i], i) in res:
            path.append(cnt + 1)
            cnt = 0
        else:
            cnt += 1
    if path:
        path[-1] += n - sum(path)

    print(ans)
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    main(10)