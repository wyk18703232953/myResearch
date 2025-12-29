import random

def main(n: int):
    # 生成测试数据：这里只是示范生成一个长度为 n 的随机数组，
    # 实际逻辑中并不使用，只是满足“根据 n 生成测试数据”的要求。
    test_data = [random.randint(1, 100) for _ in range(n)]
    # 如需查看测试数据，可取消下一行注释
    # print("Generated test data:", test_data)

    # dp 逻辑
    max_len = max(100, n)  # 保证 dp 至少有到 100 的空间，也适配 n > 100 的情况
    dp = [0] * (max_len + 1)

    # 边界条件
    if max_len >= 1:
        dp[1] = 1
    if max_len >= 2:
        dp[2] = 2

    for i in range(3, max_len + 1):
        dp[i] = dp[i - 2] + i

    # 输出原程序期望的结果：dp[n]（假设 n >= 1）
    print(dp[n])

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)