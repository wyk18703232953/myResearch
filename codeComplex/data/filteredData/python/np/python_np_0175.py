from itertools import combinations
import random

def main(n: int):
    # 生成测试数据
    # 难度范围 l 到 r，与原题意义一致
    # 这里构造：
    #   - 题目难度 a[i] 在 [1, 100] 内随机
    #   - 选题总难度和限制 l, r
    #   - 难度差限制 x
    random.seed(0)  # 固定种子以便复现，如不需要可去掉

    # 生成题目难度数组 a
    a = [random.randint(1, 100) for _ in range(n)]

    # 生成限制参数
    s = sum(a)
    if n >= 2:
        # 让 l、r 在合理区间内（至少要能选两题）
        l = random.randint(2, max(2, s // 4))
        r = random.randint(l, max(l, s))
    else:
        # 如果 n < 2，则不存在可行组合，参数随意给
        l, r = 0, 0
    x = random.randint(0, 50)

    # 原逻辑
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )

    print(ans)


# 示例调用（提交到评测系统时可注释掉）
if __name__ == "__main__":
    main(5)