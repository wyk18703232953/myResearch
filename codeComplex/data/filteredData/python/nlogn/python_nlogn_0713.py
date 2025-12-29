import random

def main(n):
    ans = ["sjfnb", "cslnb"]

    # 生成测试数据：n 个非负整数
    # 这里生成 0 到 10^9 之间的随机数，你可按需修改规则
    l = [random.randint(0, 10**9) for _ in range(n)]

    l.sort()
    d = set()
    e = 0
    s = 0
    for i in range(n):
        if l[i] in d:
            e += 1
            s = l[i]
        d.add(l[i])

    if e > 1 or l.count(0) > 1 or s - 1 in d:
        print(ans[1])
    else:
        l = [l[i] - i for i in range(n)]
        print(ans[1 - sum(l) % 2])


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n
    main(5)