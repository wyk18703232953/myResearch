from collections import deque
import random

def main(n):
    # 生成测试数据
    # N 为队列长度，Q 为查询次数
    N = n
    if N < 2:
        raise ValueError("N must be at least 2")

    Q = n  # 简单设为与 n 相同的规模
    # 生成一个包含 1..N 的随机排列作为初始队列
    arr = list(range(1, N + 1))
    random.shuffle(arr)
    que = deque(arr)

    ma = max(que)

    X = []
    k = -1
    c = 0
    # 预处理比较过程
    while c <= k + N + 5:
        a = que.popleft()
        b = que.popleft()

        X.append((a, b))
        c += 1
        if a > b:
            a, b = b, a
        if k < 0 and b == ma:
            k = c
        que.appendleft(b)
        que.append(a)

    # 构造 Q 个查询（这里简单设为查询 1..Q）
    queries = list(range(1, Q + 1))

    # 回答查询并打印
    for qi in queries:
        i = qi - 1
        if i <= k:
            print(*X[i])
        else:
            i = (i - k) % (N - 1) + k
            print(*X[i])


if __name__ == "__main__":
    # 示例：以 n = 10 作为规模运行
    main(10)