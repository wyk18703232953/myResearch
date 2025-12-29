from itertools import combinations as cmb
import random

def main(n: int) -> None:
    # 生成测试数据
    # 约束：1 ≤ n，且为了生成合理数据，设定题目参数范围
    # a[i] 在 [1, 100] 内随机生成，且保证互不相同
    a = random.sample(range(1, 101), n)
    a.sort()

    # 设置 l, r, x 的生成方式：
    # 1. 取数组最小值和最大值的差，确保 x 不会过大
    # 2. 令 l 和 r 为总和范围内的一段区间
    total_sum = sum(a)
    min_sum = a[0] + a[1]               # 至少选2个
    max_sum = total_sum                 # 最多选全部

    # 确保合法区间
    if min_sum > max_sum:
        # n < 2 时无合法选择，直接输出0
        print(0)
        return

    l = random.randint(min_sum, max_sum)
    r = random.randint(l, max_sum)
    x = random.randint(0, a[-1] - a[0] if n >= 2 else 0)

    # 原逻辑
    b = []
    for i in range(2, n + 1):
        b.extend(cmb(a, i))

    ans = 0
    for comb in b:
        s = sum(comb)
        if l <= s <= r and comb[-1] - comb[0] >= x:
            ans += 1

    print(ans)

# 示例调用
if __name__ == "__main__":
    main(5)