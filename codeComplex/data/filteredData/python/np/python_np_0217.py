from itertools import combinations
import random

def main(n: int):
    # 根据 n 生成测试数据
    # 随机生成题目参数
    # a 的元素范围设为 [1, 10^3]
    a = [random.randint(1, 1000) for _ in range(n)]

    # l, r 的范围根据 a 的总和生成，保证有一定概率存在合法区间
    total_sum = sum(a)
    l = random.randint(0, total_sum // 2)
    r = random.randint(l, total_sum)
    # x 为难度差下限
    x = random.randint(0, max(a) - min(a) if n > 1 else 0)

    # 原逻辑：计算满足条件的组合个数
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )

    print(ans)

if __name__ == "__main__":
    # 示例调用，规模可按需调整
    main(10)