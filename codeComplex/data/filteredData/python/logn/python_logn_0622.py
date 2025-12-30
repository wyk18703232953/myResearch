def check(x, n, k):
    ate = x
    rem = n - ate
    if rem * (rem + 1) // 2 == k + ate and rem >= 0 and ate >= 0:
        return True
    return False


def solve(n, k):
    b = -1 * (2 * n + 3)
    a = 1
    c = n ** 2
    c += n - (2 * k)

    d = ((b ** 2) - (4 * a * c)) ** 0.5
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)

    if check(x1, n, k):
        return int(x1)
    return int(x2)


def main(n):
    # 根据 n 生成测试数据，这里构造一个合理的 k
    # 例如令 ate = n // 2，则 k = rem*(rem+1)//2 - ate
    ate = n // 2
    rem = n - ate
    k = rem * (rem + 1) // 2 - ate

    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)