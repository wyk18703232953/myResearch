def main(n):
    # 生成测试数据：k 在 [0, n] 范围内任选一个，这里简单取 k = n // 2
    k = n // 2

    candies = 0
    summ = 0

    if k == 0:
        for i in range(n - 1, -1, -1):
            summ = summ + 1
            candies = candies + summ
            if candies == i:
                print(i)
                break
    else:
        for i in range(n - 1, -1, -1):
            summ = summ + 1
            candies = candies + summ
            if candies - i == k:
                print(i)
                break


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(10)