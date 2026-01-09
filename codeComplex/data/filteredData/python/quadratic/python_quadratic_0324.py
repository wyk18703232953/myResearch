import heapq

def main(n):
    # 这里根据 n 自动生成 d, k 的测试数据
    # 简单示例策略：让 d 和 k 都是 n 的函数，避免退化到太小的情况
    if n <= 3:
        d = max(1, n - 1)
        k = 2

    else:
        d = min(n - 1, max(2, n // 3))  # 路径长度上限
        k = min(5, max(2, n // 4))      # 每个点的度数上限

    if n == 1 or n <= d:
        ans = "NO"
        e = []
    elif k == 1:
        ans = "YES" if n == 2 and d == 1 else "NO"
        e = [(1, 2)] if ans == "YES" else []

    else:
        # 先构造一条长度为 d+1 的链
        e = [(i + 1, i + 2) for i in range(d)]
        h = []
        l, r = 1, d + 1
        if k > 2:
            for i in range(2, d + 1):
                heapq.heappush(h, (i, 2, min(i - l, r - i)))  # (节点编号, 已连接次数, 还能向外扩多少层)
        ans = "YES"
        for i in range(d + 2, n + 1):
            if not h:
                ans = "NO"
                break
            j, k0, d0 = heapq.heappop(h)
            e.append((j, i))
            if k0 + 1 < k:
                heapq.heappush(h, (j, k0 + 1, d0))
            if d0 - 1 > 0:
                heapq.heappush(h, (i, 1, d0 - 1))

    # print(ans)
    pass

    if ans == "YES":
        for u, v in e:
            # print(u, v)
            pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)