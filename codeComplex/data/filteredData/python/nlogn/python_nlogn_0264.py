import random

def main(n: int):
    # 1. 生成测试数据：n 个区间 [l, r]
    #   为保证合理性，生成 1 <= l < r <= 10^6
    intervals = []
    MAXV = 10**6
    for _ in range(n):
        l = random.randint(1, MAXV - 1)
        r = random.randint(l + 1, MAXV)
        intervals.append((l, r))

    # 2. 将原逻辑封装（去掉 input）
    a = []
    for i, (l, r) in enumerate(intervals, start=1):
        a.append([l, -r, i])

    a.sort()
    ma = a[0][1]
    nma = a[0][2]
    for i in range(1, n):
        if a[i][1] >= ma:
            print(a[i][2], nma)
            return
        else:
            ma = a[i][1]
            nma = a[i][2]
    print(-1, -1)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)