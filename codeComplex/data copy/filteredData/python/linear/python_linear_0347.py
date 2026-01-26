import heapq

def main(n):
    if n <= 0:
        # print("")
        pass
        return
    # 设定边数量 m 为 n 的两倍，保证规模随 n 线性增长
    m = 2 * n
    edges = []
    for i in range(m):
        a = i % n
        b = (i * 2 + 1) % n
        edges.append((a, b))

    # 原程序仅读取边，不使用，因此这里只是保持生成逻辑
    # 使用 heapq 以保持与原导入一致
    heap = []
    for a, b in edges:
        heapq.heappush(heap, (a, b))
    while heap:
        heapq.heappop(heap)

    ans = [0] * n
    for i in range(1, n, 2):
        ans[i] = 1
    # print(''.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(10)