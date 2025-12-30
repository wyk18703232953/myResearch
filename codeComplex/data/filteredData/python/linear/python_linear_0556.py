from collections import defaultdict
import random

def main(n):
    # 生成测试数据：长度为 n 的数组 a[1..n]，元素为 [0, 2^k-1] 范围内的随机数
    # 可根据需要修改 k 和生成规则
    k = 20  # 比较常见的设置，也可改为其他正整数
    max_val = (1 << k) - 1
    a = [0] + [random.randint(0, max_val) for _ in range(n)]

    # 以下为原逻辑
    h = defaultdict(int)
    for i in range(n):
        a[i + 1] ^= a[i]
    for i in range(n + 1):
        h[min(a[i] ^ ((1 << k) - 1), a[i])] += 1
    ans = 0
    for _, t in h.items():
        x = t // 2
        y = t - x
        ans += x * (x - 1) // 2 + y * (y - 1) // 2
    ans = (n * (n + 1)) // 2 - ans
    print(ans)


if __name__ == "__main__":
    # 示例运行：n 可在此修改
    main(10)