import bisect
import random

def main(n):
    # 生成测试数据
    # n: 士兵数量
    # q: 箭的轮数，设为 n 的两倍
    q = 2 * n

    # strength: 每个士兵的血量（1~10 的随机值）
    strength = [random.randint(1, 10) for _ in range(n)]

    # arrows: 每一轮射出的箭数量（1~10 的随机值）
    arrows = [random.randint(1, 10) for _ in range(q)]

    # 以下为原逻辑
    for i in range(1, n):
        strength[i] += strength[i - 1]

    No_arrows = 0
    last_index = n - 1

    for i in range(q):
        No_arrows += arrows[i]
        if No_arrows >= strength[-1]:
            No_arrows = 0
            print(last_index + 1)
        else:
            it = bisect.bisect_left(strength, No_arrows)
            if strength[it] == No_arrows:
                print(last_index - it)
            else:
                print(last_index - it + 1)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)