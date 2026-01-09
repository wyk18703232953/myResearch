def main(n):
    # 将 n 映射为原程序的三个参数：N, d, k
    # 这里构造一个确定性的映射：N = n, d = max(1, n // 3), k = max(2, n // 5 + 1)
    N = max(1, n)
    d = max(1, N // 3)
    if d >= N:
        d = N - 1
    k = max(2, N // 5 + 1)

    # 以下为原算法逻辑，仅将输入替换为上面的 N, d, k
    if d + 1 > N:
        # print('NO')
        pass
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
            # print('NO')
            pass
            return

    from collections import deque
    q = deque(list(range(d + 1)))
    cur = d + 1
    while q and cur < N:
        v = q.pop()
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
        # print('NO')
        pass

    else:
        # print('YES')
        pass
        for i in range(len(ans)):
            # print(*ans[i])
            pass
if __name__ == "__main__":
    # 示例：运行若干不同规模的实验
    for scale in [5, 10, 20]:
        # print(f"--- n = {scale} ---")
        pass
        main(scale)