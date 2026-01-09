def solve(n, v):
    fuel = min(n - 1, v)
    cost = fuel
    for i in range(2, n):
        if fuel >= n - 1:
            break
        fuel += 1
        cost += i
    return cost


def main(n):
    # 映射：给定规模 n，构造一对 (N, V)
    # 让 N 随规模线性增长，V 为 N 的一半（向下取整）
    if n < 2:
        N = 2

    else:
        N = n
    V = N // 2
    result = solve(N, V)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)