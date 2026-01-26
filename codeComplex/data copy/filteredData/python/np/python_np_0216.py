from itertools import combinations

def main(n):
    # 确定性生成参数 l, r, x 和数组 a
    # 让规模 n 主要体现在数组 a 的长度上
    if n < 2:
        print(0)
        return

    # 数组长度等于 n
    a = [i * 2 + (i % 3) for i in range(1, n + 1)]

    # 生成 l, r, x，使得与 a 的规模相关
    total_sum = sum(a)
    l = total_sum // 4 if total_sum >= 4 else 0
    r = total_sum // 2 if total_sum >= 2 else total_sum
    x = max(1, (a[-1] - a[0]) // 3)

    # 保持原始核心逻辑
    ans = sum(
        [
            sum(
                [
                    max(j) - min(j) >= x and l <= sum(j) <= r
                    for j in combinations(a, i)
                ]
            )
            for i in range(2, n + 1)
        ]
    )
    print(ans)

if __name__ == "__main__":
    main(10)