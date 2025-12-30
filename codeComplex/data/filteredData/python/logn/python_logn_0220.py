def d(n):
    ret = 0
    n = list(str(n))
    for i in range(len(n)):
        ret += int(n[i])
    return ret

def main(n):
    # 根据规模 n 生成测试数据：令 s = n // 2（可按需调整生成规则）
    s = n // 2

    l, h = 0, n
    for _ in range(2000):
        m = (l + h) // 2
        if m - d(m) >= s:
            h = m
        else:
            l = m

    for i in range(-100, 100):
        t = m + i
        if t < 0 or t > n:
            continue
        if abs(t - d(t)) >= s:
            print(n - t + 1)
            return
    print(0)


if __name__ == '__main__':
    # 示例：调用 main(10**6)
    main(10**6)