def main(n):
    # 映射 n -> (N, d, k) 保持确定性
    # 保证 N >= 1, d >= 0, k >= 1 且 d < N
    if n < 1:
        n = 1
    N = n
    d = (n // 3) % max(1, N)  # 0 <= d < N
    if d + 1 > N:
        d = max(0, N - 1)
    k = max(1, (n // 2) % (N + 2))

    if d + 1 > N:
        print('NO')
        return

    ans = []
    dist = [0] * N
    deg = [0] * N
    for i in range(d + 1):
        if i == 0 or i == d:
            deg[i] = 1
        else:
            deg[i] = 2
        if i != d:
            ans.append((i + 1, i + 2))
        dist[i] = max(i, d - i)

    for i in range(N):
        if deg[i] > k:
            print('NO')
            return

    from collections import deque
    q = deque(list(range(d + 1)))
    cur = d + 1
    while q and cur < N:
        v = q.popleft()
        if dist[v] < d and deg[v] < k:
            deg[v] += 1
            dist[cur] = dist[v] + 1
            deg[cur] = 1
            ans.append((v + 1, cur + 1))
            q.append(v)
            q.append(cur)
            cur += 1
        else:
            continue
    if cur != N:
        print('NO')
    else:
        print('YES')
        for i in range(len(ans)):
            print(*ans[i])


if __name__ == "__main__":
    # 示例：使用一个固定 n 调用，保证可重复实验
    main(10)