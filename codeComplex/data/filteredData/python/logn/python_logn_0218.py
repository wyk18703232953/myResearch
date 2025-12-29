def nine(p):
    s = ''
    for _ in range(p):
        s += '9'
    return int(s)


def prosh(p):
    ans = 0
    for i in range(1, p + 1):
        ans += nine(i) * 9
    return ans


def main(n):
    # 生成与规模 n 对应的测试数据：
    # 为了演示，这里令 k = prosh(min(n, 19))
    # （原代码中只用到长度最多 19 的 9 串）
    max_len = 19
    t = min(n, max_len)
    k = prosh(t)

    l = [0] * 29
    for i in range(19):
        e = nine(19 - i)
        l[i] = k // e
        k -= l[i] * e

        if k == 0:
            break
        if i == 18 or k % e > prosh(19 - i - 1):
            l[i] += 1
            break

    otv = 0
    for i in range(19):
        otv += 10 ** (19 - i) * l[i]

    # 原程序输出
    print(max(n - otv + 1, 0))


if __name__ == "__main__":
    # 示例：调用 main，n 可按需调整
    main(10)