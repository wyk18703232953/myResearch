import random

def main(n):
    # 生成一组自洽的 za，然后根据题意构造 zl, zr 再跑原逻辑

    # 1. 随机生成一个 za（1..n 的任意排列 or 重复值都可，这里用 1..n 的排列）
    za = list(range(1, n + 1))
    random.shuffle(za)

    # 2. 按题意定义 zl, zr
    zl = [0] * n
    zr = [0] * n
    for i in range(n):
        # 左边大于 za[i] 的数量
        l = 0
        for j in range(i):
            if za[j] > za[i]:
                l += 1
        # 右边大于 za[i] 的数量
        r = 0
        for j in range(i + 1, n):
            if za[j] > za[i]:
                r += 1
        zl[i] = l
        zr[i] = r

    # 3. 用原程序逻辑，从 zl, zr 重新推导 za2 并检验
    N = n
    zt = [(zl[i] + zr[i], i) for i in range(N)]
    zt.sort()
    za2 = [0] * N
    now = N
    for i in range(N):
        if i > 0 and zt[i - 1][0] < zt[i][0]:
            now -= 1
        za2[zt[i][1]] = now

    for i in range(N):
        l = 0
        r = 0
        for j in range(i):
            if za2[j] > za2[i]:
                l += 1
        for j in range(i + 1, N):
            if za2[j] > za2[i]:
                r += 1
        if zl[i] != l or zr[i] != r:
            print('NO')
            return

    print('YES')
    for x in za2:
        print(x, end=' ')
    print()


if __name__ == "__main__":
    # 示例：n = 5
    main(5)