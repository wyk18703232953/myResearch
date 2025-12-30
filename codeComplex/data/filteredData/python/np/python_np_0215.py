import itertools
import random

def main(n):
    # 生成测试数据
    # C 为 n 个正整数，范围 [1, 10^6]
    C = [random.randint(1, 10**6) for _ in range(n)]
    C.sort()
    # 生成限制条件
    total_sum = sum(C)
    min_val, max_val = C[0], C[-1]
    # l, r 在 [0, total_sum]，且 l <= r
    l = random.randint(0, total_sum // 2)
    r = random.randint(l, total_sum)
    # x 在 [0, max_val - min_val]
    x = random.randint(0, max_val - min_val if max_val > min_val else 0)

    ans = 0
    for k in range(2, n + 1):
        for c in itertools.combinations(C, k):
            d = sum(c)
            if d < l or d > r:
                continue
            if max(c) - min(c) < x:
                continue
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)