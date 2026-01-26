from itertools import combinations

def main(n):
    # 映射：n 为题目中的 n，同时用于生成确定性数据
    l = max(1, n // 3)
    r = max(l, (2 * n) // 3)
    x = max(1, n // 4)
    c = [i * 2 + (i % 3) for i in range(1, n + 1)]

    ans = sum(
        1
        for i in range(1, n + 1)
        for j in combinations(c, i)
        if max(j) - min(j) >= x and l <= sum(j) <= r
    )
    print(ans)
    return ans

if __name__ == "__main__":
    main(10)