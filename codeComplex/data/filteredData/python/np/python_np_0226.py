from itertools import combinations
import random

def main(n: int) -> None:
    # 生成测试数据
    # 假设题意为：从 n 个难度值中选题，约束为：
    #   - 每个难度在 [1, 10^6] 范围内
    #   - l, r 为总难度的下界、上界
    #   - x 为题目最大难度与最小难度的差值下界
    #
    # 这里给出一份合理的自动生成逻辑，可按需要调整：
    random.seed(0)  # 固定随机种子，保证复现性
    a = [random.randint(1, 10**6) for _ in range(n)]
    # 为了让约束具备一定合理性，构造 l, r, x
    total_sum = sum(a)
    max_a = max(a)
    min_a = min(a)
    # 保证 l <= r
    l = random.randint(0, total_sum // 2 if total_sum > 0 else 0)
    r = random.randint(l, total_sum)
    # x 不超过当前难度跨度
    x = random.randint(0, max_a - min_a if max_a > min_a else 0)

    # 原始逻辑
    sumu = 0
    for i in range(2, n + 1):
        for j in combinations(a, i):
            s = sum(j)
            if l <= s <= r and (max(j) - min(j) >= x):
                sumu += 1

    print(sumu)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)