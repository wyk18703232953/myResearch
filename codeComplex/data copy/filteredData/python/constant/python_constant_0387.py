def f(ch):
    if ch == '0':
        return 0

    else:
        return 1


def main(n):
    # n 表示每一行的长度（规模）
    # 构造两个长度为 n 的 0/1 字符串，完全确定性
    # 第一行：周期模式 "0011"
    s0 = ''.join('0' if (i % 4) < 2 else '1' for i in range(n))
    # 第二行：周期模式 "0101"
    s1 = ''.join('0' if (i % 2) == 0 else '1' for i in range(n))

    U = [
        [f(ch) for ch in s0],
        [f(ch) for ch in s1]
    ]

    i = 0
    size = len(U[0])
    ans = 0
    while i + 1 < size:
        s = U[0][i] + U[0][i + 1] + U[1][i] + U[1][i + 1]
        if s > 1:
            i += 1
            continue
        elif s == 1:
            U[0][i] = 1
            U[0][i + 1] = 1
            U[1][i] = 1
            U[1][i + 1] = 1
            ans += 1

        else:
            U[0][i] = 1
            U[0][i + 1] = 1
            U[1][i] = 1
            ans += 1
        i += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)