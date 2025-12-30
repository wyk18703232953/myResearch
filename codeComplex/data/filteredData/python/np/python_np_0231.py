from itertools import combinations
import random

def main(n):
    # 生成测试数据
    # 保持题意：n 个数，区间 [l, r]，难度差至少 x
    # 这里简单构造：
    #   li 为 1 到 100 之间的随机数
    #   l, r 根据 li 的总和和 n 构造一个合理区间
    #   x 为一个适中的差值
    random.seed(0)  # 固定随机种子，保证可复现
    li = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(li)
    avg = total_sum // n if n > 0 else 0

    # 构造区间 [l, r]：
    # l 从平均值附近开始，r 不超过总和
    l = max(0, avg - 10)
    r = min(total_sum, avg * 3 + 50)

    # 构造 x 为约四分之一的最大差值潜力
    max_val, min_val = max(li), min(li)
    x = max(1, (max_val - min_val) // 4)

    ans = 0
    for k in range(2, n + 1):
        for comb in combinations(li, k):
            a = sorted(comb)
            s = sum(a)
            if a[-1] - a[0] >= x and l <= s <= r:
                ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例调用：可自行修改 n
    main(5)