from collections import deque

def main(n):
    # 规模含义：
    # n >= 2 时：
    #   - 数组长度 = n
    #   - q = n（查询次数）
    #   - 初始数组 a = [1, 2, ..., n]
    # n <= 1 时，算法本身无意义，这里直接返回
    if n <= 1:
        return

    # 构造原始输入
    q = n
    a = deque(range(1, n + 1))

    # 原算法主体
    b = []
    m = a.index(max(a))
    for _ in range(m):
        a0, a1 = a.popleft(), a.popleft()
        b.append([a0, a1])
        if a0 < a1:
            a0, a1 = a1, a0
        a.appendleft(a0)
        a.append(a1)

    # 构造确定性的查询序列：
    # 使用原来典型的 1..q 顺序查询
    queries = list(range(1, q + 1))

    for c in queries:
        if c <= m:
            # print('{} {}'.format(b[c - 1][0], b[c - 1][1]))
            pass

        else:
            c_adj = c - (m + 1)
            c_adj %= n - 1
            # print('{} {}'.format(a[0], a[c_adj + 1]))
            pass
if __name__ == "__main__":
    # 示例：对若干规模运行一遍
    for size in [2, 3, 5, 10]:
        # print("n =", size)
        pass
        main(size)