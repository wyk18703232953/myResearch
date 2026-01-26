from itertools import combinations

def main(n):
    # 解释规模含义：
    # n 表示数组 a 的长度
    # 其他参数 l, r, x 按固定规则由 n 确定性生成
    if n < 2:
        print(0)
        return

    # 确定性构造参数
    l = n              # 下界
    r = 3 * n          # 上界
    x = n // 2 + 1     # 最大最小差值下限

    # 确定性构造数组 a，元素值随索引线性变化
    a = [i % (2 * n) + 1 for i in range(1, n + 1)]

    ans = sum(
        sum(
            max(j) - min(j) >= x and l <= sum(j) <= r
            for j in combinations(a, i)
        )
        for i in range(2, n + 1)
    )
    print(ans)


if __name__ == "__main__":
    main(10)