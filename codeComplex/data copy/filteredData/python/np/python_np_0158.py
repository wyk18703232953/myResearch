from itertools import combinations

def main(n):
    # 解释：n 作为数组长度规模
    # 构造确定性的数组 a，元素值随索引线性增长
    a = [i * 2 + 1 for i in range(n)]

    # 为了让规模随 n 合理增长，设置区间和差值阈值
    # l、r 与 n 成比例，x 为固定常数
    l = n
    r = n * (n + 1)
    x = n // 2 if n > 0 else 0

    ans = 0
    for i in range(2, n + 1):
        for j in combinations(a, i):
            if max(j) - min(j) >= x and l <= sum(j) <= r:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main(10)