m = int(1e9 + 7)


def solve(x, k):
    return (
        m
        + (pow(2, k, m) * x % m) % m
        - ((pow(2, k, m) - 1) % m * pow(2, m - 2, m) % m) % m
    ) % m


def main(n):
    # 根据规模 n 生成测试数据：
    # 用 n 控制 x 和 k 的大小（这里简单用 n 本身及其平方作为示例）
    x = n
    k = n * n

    if x == 0:
        ans = 0
    elif k == 0:
        ans = (m + 2 * (x % m)) % m
    else:
        ans = (m + 2 * solve(x, k)) % m

    print(ans)


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(10)