from collections import deque

def main(n):
    # 映射规则：
    # n >= 2
    # 数组长度: N = n
    # 查询数量: Q = n
    if n < 2:
        n = 2

    N = n
    Q = n

    # 确定性构造数组 a:
    # 让最大值在中间附近，并确保唯一最大值
    # a[i] = (i * 2 + 1) % (2 * N) + 1，最后一个元素替换为 2*N+1 作为唯一最大值
    base = [(i * 2 + 1) % (2 * N) + 1 for i in range(N)]
    base[-1] = 2 * N + 1
    a = deque(base)

    # 确定性构造查询序列:
    # 1..Q，覆盖小于等于 m、大于 m 的各种情况
    queries = list(range(1, Q + 1))

    b = []
    m = a.index(max(a))
    for _ in range(m):
        a0, a1 = a.popleft(), a.popleft()
        b.append([a0, a1])
        if a0 < a1:
            a0, a1 = a1, a0
        a.appendleft(a0)
        a.append(a1)

    outputs = []
    for c in queries:
        if c <= m:
            outputs.append(f"{b[c-1][0]} {b[c-1][1]}")

        else:
            c_adj = c - (m + 1)
            c_adj %= (N - 1)
            outputs.append(f"{a[0]} {a[c_adj + 1]}")

    for line in outputs:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)