import random

def main(n):
    # 生成测试数据
    # n: 数组长度
    # k: 分组数量，1 <= k <= n
    k = random.randint(1, n)
    # 生成一个严格递增数组 a，满足原代码对差分的语义
    a = [0]
    for _ in range(n - 1):
        a.append(a[-1] + random.randint(1, 10))

    # 原逻辑
    d = [a[i + 1] - a[i] for i in range(n - 1)]
    ans = sum(sorted(d)[:n - 1 - (k - 1)])
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(10)