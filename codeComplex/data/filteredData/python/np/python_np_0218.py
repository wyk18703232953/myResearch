from itertools import combinations

def main(n):
    # 根据 n 构造确定性的输入规模和参数
    # 约束：n 至少为 2
    if n < 2:
        n = 2

    # 原程序中的 n：题目规模，这里设为 n
    N = n

    # 构造数组 a：使用简单等差序列，元素互不相同且随 n 线性增长
    a = [i for i in range(1, N + 1)]

    # 构造区间 [l, r] 和差值 x，使得有一定数量的合法组合
    # l 设为总和的大约 1/4，r 设为总和的 3/4，x 设为 N//4
    total_sum = N * (N + 1) // 2
    l = total_sum // 4
    r = (total_sum * 3) // 4
    x = max(1, N // 4)

    ans = 0
    for i in range(2, N + 1):
        for p in combinations(a, i):
            s = sum(p)
            if l <= s <= r and max(p) - min(p) >= x:
                ans += 1

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次运行
    main(10)