from itertools import combinations

def main(n):
    # 参数含义与原题保持一致：
    # n: 题目中题目数量
    # l, r, x: 由 n 确定性生成
    # a: 长度为 n 的整数列表，确定性生成

    # 确定性生成 l, r, x
    # 保证 l <= r，并让区间规模随 n 增长
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # 确定性生成长度为 n 的数组 a
    # 元素递增且分布简单，便于规模化分析
    a = [i + 1 for i in range(n)]

    arr = []

    for i in range(2, n + 1):
        ar = combinations(a, i)
        for j in ar:
            arr.append(list(j))

    count = 0
    for subset in arr:
        dif = max(subset) - min(subset)
        total = sum(subset)
        if dif >= x and l <= total <= r:
            count += 1

    print(count)


if __name__ == "__main__":
    main(10)