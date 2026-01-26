from math import log

def main(n: int):
    k = n  # 原程序中的 k 即为规模 n
    r = k
    l = 1
    t = log(10)
    while True:
        m = (l + r) // 2
        x = int(log(m) / t)
        d = ((1 - 10 ** (x + 1)) // 9) + (m + 1) * (x + 1)
        if 0 <= (k - d) <= 13:
            break
        elif d > k:
            r = m - 1

        else:
            l = m + 1

    if m == 1000:
        d += 1

    if d == k:
        # print(str(m)[-1])
        pass
        return

    st = ""
    v = k - d
    m += 1
    for _ in range(13):
        st += str(m)
        m += 1
    # print(st[v - 1])
    pass
if __name__ == "__main__":
    # 示例：调用 main 并使用 n 作为规模参数
    # 可根据需要修改 n 的值进行测试
    n = 123456
    main(n)