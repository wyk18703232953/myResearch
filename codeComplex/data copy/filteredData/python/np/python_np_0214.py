from itertools import combinations

def main(n):
    # 映射：p = n，列表长度为 p，元素为 1..p
    p = max(2, n)
    minn = p          # 下界
    maxn = p * (p + 1) // 2  # 上界取前 p 个数之和，保证覆盖
    dif = 1           # 最小差值
    lst = list(range(1, p + 1))

    total = 0
    for i in range(2, p + 1):
        for j in combinations(lst, i):
            s = sum(j)
            if maxn >= s >= minn and (max(j) - min(j)) >= dif:
                total += 1
    print(total)


if __name__ == "__main__":
    main(10)