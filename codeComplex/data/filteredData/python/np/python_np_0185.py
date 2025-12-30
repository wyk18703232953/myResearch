from itertools import combinations
import random


def main(n: int) -> int:
    """
    n: 问题规模，这里用于生成 n 个元素的数组 c。
    返回：满足原题条件的方案数 k。
    """

    # 根据 n 生成测试数据
    # 约束示例：
    #   c 为 n 个不同的正整数（类似竞赛题常见设定）
    #   l, r 为区间下界和上界
    #   x 为极差下界
    random.seed(0)  # 为可复现性固定随机种子，可按需要移除
    c = sorted(random.sample(range(1, max(2 * n, 10) + 1), n))

    # 生成 l, r, x，使得：
    #   l 不大于所有元素和
    #   r 大于等于 l
    total_sum = sum(c)
    l = random.randint(1, max(1, total_sum // 2))
    r = random.randint(l, total_sum)
    # x 尝试设为中等大小
    max_diff = c[-1] - c[0]
    x = random.randint(0, max_diff)

    # 原逻辑开始
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (c[j] - c[i]) >= x:
                if sum(c[i:j + 1]) < l:
                    continue
                elif (c[i] + c[j]) > r:
                    continue
                else:
                    if l <= (c[i] + c[j]) <= r:
                        k += 1
                    for p in range(1, j - i):
                        for m in combinations(c[i + 1:j], p):
                            s = sum(m) + c[i] + c[j]
                            if l <= s <= r:
                                k += 1

    print(k)
    return k


if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)