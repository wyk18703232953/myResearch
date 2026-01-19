from itertools import combinations

def main(n):
    # 解释规模含义：
    # n 表示数组 a 的长度，同时也是原程序中的 n
    # 为保证可运行，n 至少为 2
    if n < 2:
        n = 2

    # 确定性生成原输入数据
    # a 为长度为 n 的整数数组
    a = [i * 2 + 1 for i in range(1, n + 1)]

    # 生成其他标量参数
    # l, r 构造为关于 n 的确定性区间，x 为确定性阈值
    total_sum = sum(a)
    l = total_sum // 4
    r = total_sum // 2 + 1
    x = n // 2 + 1

    # 原算法逻辑
    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )
    print(ans)
    return ans

if __name__ == "__main__":
    main(10)