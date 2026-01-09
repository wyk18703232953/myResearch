def main(n: int):
    # 预计算足够长的 Fibonacci 序列，直到超过 n 即可
    fib = [0, 1]
    while fib[-1] < n and len(fib) < 1000:
        fib.append(fib[-1] + fib[-2])

    if n in fib:
        idx = fib.index(n)
        if n == 0:
            # print(0, 0, 0)
            pass
        elif n == 1:
            # print(0, 0, 1)
            pass

        else:
            # print(0, fib[idx - 2], fib[idx - 1])
            pass

    else:
        # print("I'm too stupid to solve this problem")
        pass
if __name__ == "__main__":
    # 这里根据规模 n 生成测试数据
    # 例如：n 越大，测试的 Fibonacci 目标值越大
    # 你可以自行调整生成逻辑
    test_n = 0
    # 示例：按规模选取一个 Fibonacci 数作为测试
    # 生成前 n+3 个 Fibonacci，然后取第 n 个（防止索引过小）
    fib_test = [0, 1]
    for _ in range(n := max(1, 10)):  # 默认规模 10，可按需修改
        fib_test.append(fib_test[-1] + fib_test[-2])
    test_n = fib_test[n]  # 取一个一定是 Fibonacci 的数

    main(test_n)