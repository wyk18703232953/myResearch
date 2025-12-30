from collections import defaultdict as dc
import random

def main(n: int) -> None:
    # 生成测试数据
    # 这里设定 m = n * k，k 为常数倍，可按需要调整
    k = 3
    m = n * k
    # 生成长度为 m 的序列，每个元素在 1..n 之间
    l = [random.randint(1, n) for _ in range(m)]

    x = dc(int)
    p = 0

    for val in l:
        x[val] += 1
        f = 1
        # 检查 1..n 是否都至少出现一次
        for i in range(1, n + 1):
            if x[i] == 0:
                f = 0
                break
        if f:
            p += 1
            # 每个数都“消耗”一次
            for i in range(1, n + 1):
                x[i] -= 1

    print(p)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)