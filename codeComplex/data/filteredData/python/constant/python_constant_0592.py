def main(n):
    # 这里的 k 原本来自输入，为了生成测试数据，可以设定为 n 的某个函数
    # 示例：令 k = n + 1（确保 k > 0）
    k = n + 1

    ans = 0
    ans += (2 * n) // k + int((2 * n) % k != 0)
    ans += (5 * n) // k + int((5 * n) % k != 0)
    ans += (8 * n) // k + int((8 * n) % k != 0)
    print(ans)


if __name__ == "__main__":
    # 示例测试：生成规模 n 的测试数据并运行
    # 可按需修改 n 的取值
    n = 10
    main(n)