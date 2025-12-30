import random

def main(n):
    # 生成测试数据：n 行，m 列
    # 这里设置 m 为一个相对固定的小规模（例如 5），也可根据需要调整或与 n 关联
    m = max(1, min(10, n))  # 简单设置：m 不超过 10，且至少为 1
    # 生成 arr[n][m]，取值范围 [0, 1e9]
    arr = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    x = 1
    N = (1 << m) - 1
    lo = 1
    hi = 1000000009
    ind = [0, 0]

    while True:
        l = {}
        freq = [0] * (1 << m)
        for i in range(n):
            an = 0
            for j in range(m):
                if arr[i][j] >= x:
                    an += 1 << (m - j - 1)
            if freq[an] == 0:
                l[i] = an
            freq[an] = 1

        ch = 0
        for k1, v1 in l.items():
            for k2, v2 in l.items():
                if (v1 | v2) == N:
                    ch = 1
                    ind[0] = k1 + 1
                    ind[1] = k2 + 1
                    break
            if ch:
                break

        if ch:
            lo = x
            x = x * 2
        else:
            hi = x
            break

    while hi - lo > 1:
        x = (lo + hi) // 2
        l = {}
        freq = [0] * (1 << m)
        for i in range(n):
            an = 0
            for j in range(m):
                if arr[i][j] >= x:
                    an += 1 << (m - j - 1)
            if freq[an] == 0:
                l[i] = an
            freq[an] = 1

        ch = 0
        for k1, v1 in l.items():
            for k2, v2 in l.items():
                if (v1 | v2) == N:
                    ch = 1
                    ind[0] = k1 + 1
                    ind[1] = k2 + 1
                    break
            if ch:
                break

        if ch:
            lo = x
        else:
            hi = x

    if ind[0] == 0:
        print("1 1")
    else:
        print(*ind)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)