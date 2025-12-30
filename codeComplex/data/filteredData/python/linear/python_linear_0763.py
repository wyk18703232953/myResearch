from collections import deque
import random


def main(n):
    # 生成规模为 n 的测试数据
    # 约定：m 为查询次数，这里设为 2 * n（可按需调整）
    m = 2 * n

    # 生成一个长度为 n 的随机排列，作为初始队列
    nums = list(range(1, n + 1))
    random.shuffle(nums)

    # 生成 m 个查询，每个查询 q 的范围大致在 [1, 3 * n] 内
    # 这样可以覆盖 q <= rot 和 q > rot 的两种情况
    queries = [random.randint(1, 3 * n) for _ in range(m)]

    # 以下是原逻辑的封装与运行
    mxnum = max(nums)
    d = deque(nums)

    qr = queries[:]  # 查询拷贝（可直接用 queries）

    log = []
    rot = 0
    while True:
        a = d.popleft()
        b = d.popleft()
        log.append((a, b))
        if a > b:
            a, b = b, a

        d.append(a)
        d.appendleft(b)

        rot += 1

        if b == mxnum:
            break

    # 输出：每次查询对应的结果
    for q in qr:
        if q <= rot:
            print(log[q - 1][0], log[q - 1][1])
        else:
            res = q - rot - 1
            print(b, d[res % (n - 1) + 1])


# 示例：当做脚本运行时执行 main，规模可自行调整
if __name__ == "__main__":
    main(5)