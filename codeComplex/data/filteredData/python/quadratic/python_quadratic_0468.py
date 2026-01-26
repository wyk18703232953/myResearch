import sys

def main(n):
    # n 表示 N 的规模
    N = max(1, int(n))

    # 生成一个确定性的 za 序列
    # 这里选择 za[i] = N - i，保证严格递减且易于分析
    za = [N - i for i in range(N)]

    # 根据算法逻辑倒推 zl, zr，使得后续验证必然通过
    zl = [0] * N
    zr = [0] * N
    for i in range(N):
        l = 0
        r = 0
        for j in range(i):
            if za[j] > za[i]:
                l += 1
        for j in range(i + 1, N):
            if za[j] > za[i]:
                r += 1
        zl[i] = l
        zr[i] = r

    # 以下是原始程序逻辑，不依赖输入
    zt = [(zl[i] + zr[i], i) for i in range(N)]
    zt.sort()
    za2 = [0 for _ in range(N)]
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
            # print('NO')
            pass
            return
    # print('YES')
    pass
    for i in range(N):
        # print(za2[i], end=' ')
        pass
    if N > 0:
        # print()
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行实验
    main(10)