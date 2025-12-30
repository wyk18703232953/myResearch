def d(num: int) -> int:
    ret = 0
    num = list(str(num))
    for i in range(len(num)):
        ret += int(num[i])
    return ret


def solve(n: int, s: int) -> int:
    l, h = 0, n
    for _ in range(2000):
        m = (l + h) // 2
        if m - d(m) >= s:
            h = m
        else:
            l = m
    # 局部微调，寻找最小满足条件的 t
    for i in range(-100, 100):
        t = m + i
        if t < 0 or t > n:
            continue
        if abs(t - d(t)) >= s:
            return n - t + 1
    return 0


def main(n: int) -> int:
    # 根据规模 n 生成测试数据，这里构造 s 为 n 的一半（可按需求调整）
    # 原问题中通常有 0 <= s <= n 的约束
    s = max(0, n // 2)
    return solve(n, s)


if __name__ == '__main__':
    # 简单示例：调用 main(100000)
    ans = main(100000)
    print(ans)