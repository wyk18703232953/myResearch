import random

def main(n):
    # 生成测试数据
    # people: 组数上限，设为 n
    people = n

    # 生成 n 个整数，范围 1..min(10000, n)
    max_val = min(10000, max(1, n))
    a = [random.randint(1, max_val) for _ in range(n)]

    # 原逻辑开始
    a.sort()
    d = {}
    tmp = []
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    d1 = {}
    for i in d:
        if d[i] in d1:
            d1[d[i]] += 1
        else:
            d1[d[i]] = 1
        tmp.append(d[i])

    tmp.sort()
    ans = 0
    for i in range(1, 10001):
        x = people
        try:
            x -= d1[i]
        except KeyError:
            pass
        for j in d1:
            if j > i:
                x -= (j // i) * d1[j]
        if x <= 0:
            ans = max(ans, i)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(1000)
    main(1000)