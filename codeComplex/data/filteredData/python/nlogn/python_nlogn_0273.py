import random

def solve(a):
    aa = sorted(a)
    maxr = aa[0]
    for ai in aa:
        if ai[2] != maxr[2]:
            if ai[1] <= maxr[1] and ai[0] >= maxr[0]:
                return (ai[2], maxr[2])
            if ai[1] >= maxr[1] and ai[0] <= maxr[0]:
                return (maxr[2], ai[2])
        if ai[1] > maxr[1]:
            maxr = ai
    return (-1, -1)

def main(n):
    # 生成测试数据：n 个区间 [l, r]，1 <= l <= r <= 10^6
    a = []
    for i in range(n):
        l = random.randint(1, 10**6)
        r = random.randint(l, 10**6)
        a.append((l, r, i + 1))

    i, j = solve(a)
    print(i, j)

if __name__ == "__main__":
    # 示例：规模为 10，可以根据需要修改
    main(10)