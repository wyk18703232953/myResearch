import math
import random

def main(n: int):
    # 生成测试数据 n, m, k, l
    # 保证 m >= 1，且尽量让部分用例有解、部分无解
    if n <= 0:
        print(-1)
        return

    # m 至少为 1，最多为 n
    m = random.randint(1, max(1, n))

    # 先随机生成一个 k + l 的目标值 S
    # 让 S 在 [0, 2n] 范围内，有一定概率 > n，从而触发 -1 分支
    S = random.randint(0, 2 * n)

    # 在 [0, S] 中随机切一刀，得到 k 和 l
    k = random.randint(0, S)
    l = S - k

    # 原逻辑开始
    t = int(k + l + m - 1) // m  # 向上取整

    if k + l > n:
        print(-1)
        return

    if m * t > n:
        print(-1)
        return

    print(t)

if __name__ == '__main__':
    # 示例：调用 main(n) 进行测试，可根据需要修改 n
    main(100)