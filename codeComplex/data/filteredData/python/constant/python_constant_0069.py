def main(n: int):
    fib = [0, 1]

    # 生成不超过 n 的斐波那契数列
    for x in range(1, 200):
        z = fib[x] + fib[x - 1]
        if z <= n:
            fib.append(z)
        else:
            break

    fib = fib[::-1]
    lis = []

    # 贪心选取不超过 n 的三个斐波那契数
    for y in range(len(fib)):
        if fib[y] <= n and (sum(lis) + fib[y]) <= n and len(lis) < 3:
            lis.append(fib[y])

    if sum(lis) == n:
        if len(lis) == 1:
            lis.append(0)
            lis.append(0)
            print(*lis)
        elif len(lis) == 2:
            lis.append(0)
            print(*lis)
        else:
            print(*lis)
    else:
        print("I'm too stupid to solve this problem")


# 示例自动生成测试数据并调用
if __name__ == "__main__":
    # 这里根据需要生成规模为 n 的测试数据
    # 示例：取一个中等规模的 n
    test_n = 1000
    main(test_n)