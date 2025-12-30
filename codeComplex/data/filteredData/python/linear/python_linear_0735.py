from collections import deque
import random


def main(n):
    # 1. 随机构造数据规模
    # n: 序列长度
    # q: 查询次数（这里取与 n 同级，可按需调整）
    q = n

    # 2. 构造初始序列 S
    # 为了避免所有元素都相等影响测试效果，这里构造 1..n 的随机排列
    S = list(range(1, n + 1))
    random.shuffle(S)

    # 3. 按原逻辑模拟前 n 步操作
    Q = deque(S)
    res = []

    for _ in range(n):
        a = Q.popleft()
        b = Q.popleft()
        if a > b:
            Q.appendleft(a)
            Q.append(b)
        else:
            Q.appendleft(b)
            Q.append(a)
        res.append((a, b))

    A = list(Q)

    def solve(t):
        # t 从 1 开始
        if t <= len(res):
            return res[t - 1]
        t -= len(res) + 1
        t %= n - 1
        return A[0], A[t + 1]

    # 4. 构造 q 个查询并输出结果
    # 这里让查询编号从 1 到 q，覆盖前缀和周期部分
    for t in range(1, q + 1):
        x, y = solve(t)
        print(x, y)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时请按需修改 n
    main(10)