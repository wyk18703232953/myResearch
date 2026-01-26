import sys
from collections import deque

def main(n):
    # 解释 n 的含义：
    # N: 队列长度（至少 2）
    # Q: 查询次数（至少 1）
    # 这里构造一个确定性的关系：N = max(2, n)，Q = max(1, n)
    N = max(2, n)
    Q = max(1, n)

    # 构造初始队列：1, 2, ..., N
    que = deque(range(1, N + 1))
    ma = max(que)

    X = []
    k = -1
    c = 0
    # 原逻辑：模拟直到找到最大值到达特定位置并多跑一些步
    while c <= k + N + 5:
        a = deque.popleft(que)
        b = deque.popleft(que)

        X.append((a, b))
        c += 1
        if a > b:
            a, b = b, a
        if k < 0 and b == ma:
            k = c
        deque.appendleft(que, b)
        deque.append(que, a)

    # 构造 Q 个查询，下标从 1 开始，确定性为 1..Q
    queries = list(range(1, Q + 1))

    out_lines = []
    for i in queries:
        i -= 1
        if i <= k:
            out_lines.append(f"{X[i][0]} {X[i][1]}")

        else:
            idx = (i - k) % (N - 1) + k
            out_lines.append(f"{X[idx][0]} {X[idx][1]}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)