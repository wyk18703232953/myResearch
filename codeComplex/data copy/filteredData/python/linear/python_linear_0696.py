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
    # 对于规模 n，构造一组 (nn, v) 输入：
    # nn 为问题中的 n，v 为油量限制，均为 n 的确定性函数
    if n <= 1:
        nn = 1
        v = 0

    else:
        nn = n
        v = n // 2
    result = solve(nn, v)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)