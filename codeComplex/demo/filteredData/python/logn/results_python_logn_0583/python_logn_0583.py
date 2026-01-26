def formula(n, x):
    return x * (x + 1) // 2 - (n - x)


def solve(n, k):
    l = 1
    r = n
    x = 0
    while l <= r:
        x = (l + r) // 2
        res = formula(n, x)
        if res == k:
            break
        elif res < k:
            l = x + 1

        else:
            r = x - 1
    # print(n - x)
    pass


def main(n):
    # 生成测试数据：
    # 为了保证存在解，这里先随机选一个 x，再计算对应的 k
    # 也可以改成其它形式的生成逻辑，只要保证 k 合法即可
    if n <= 0:
        return

    # 简单起见，选取中间的 x
    x = n // 2 if n // 2 >= 1 else 1
    k = formula(n, x)

    solve(n, k)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)