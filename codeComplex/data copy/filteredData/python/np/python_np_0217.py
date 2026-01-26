from itertools import combinations

def main(n):
    # 将 n 视为题目中的 n（元素个数），并构造确定性数据
    if n < 2:
        print(0)
        return
    l = n
    r = 3 * n
    x = n // 2 if n >= 2 else 1
    a = [i + 1 for i in range(n)]
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