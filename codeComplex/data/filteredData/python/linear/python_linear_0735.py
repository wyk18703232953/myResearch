from collections import deque

def main(n):
    # n 控制队列规模和查询数量，最小为 2
    if n < 2:
        n = 2

    # 构造确定性的初始队列 S，长度为 n
    # 示例：S = [1, 2, 3, ..., n]
    S = [i + 1 for i in range(n)]

    # 构造确定性的查询列表 Ts，长度也为 n
    # 令查询时间在 [1, n^2] 范围内循环
    max_t = n * n
    Ts = [(i * n + 1) for i in range(n)]
    Ts = [t if t <= max_t else ((t - 1) % max_t) + 1 for t in Ts]

    Q = deque(S)
    length = len(Q)

    res = []
    for _ in range(length):
        a = Q.popleft()
        b = Q.popleft()
        Q.appendleft(max(a, b))
        Q.append(min(a, b))
        res.append((a, b))

    A = list(Q)

    def solve(t):
        if t < len(res):
            return res[t - 1]
        t -= len(res) + 1
        t %= length - 1
        return A[0], A[t + 1]

    outputs = []
    for t in Ts:
        outputs.append(solve(t))

    # 输出结果以便进行时间复杂度实验
    for a, b in outputs:
        print(a, b)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    main(10)