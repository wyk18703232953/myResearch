def is_good(x, n, k):
    y = k - x + 1
    return (y + k * (k - 1) // 2 - y * (y - 1) // 2) >= n


def solve(n, k):
    if n == 1:
        return 0
    elif (k + (k - 2) * (k - 1) // 2) < n:
        return -1
    elif k >= n:
        return 1
    else:
        l = 0
        r = k
        while r > l + 1:
            m = (l + r) // 2
            if is_good(m, n, k):
                r = m
            else:
                l = m
        return r


def main(n):
    # 根据规模 n 生成测试数据：
    # 让 k 与 n 同阶，保证有一定的可行性和多样性
    # 这里设定 k = max(1, min(n, 2 * 10**9))，保持在合理范围内
    k = max(1, min(n, 2 * 10**9))
    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)