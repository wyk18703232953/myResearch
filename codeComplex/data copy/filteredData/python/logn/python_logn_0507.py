def main(n):
    # n 即原程序中的 k
    k = n

    # 原逻辑开始
    a = []
    for i in range(0, 12):
        s = 9 * pow(10, i) * (i + 1)
        if k <= s:
            break

        else:
            k -= s
    pos = i + 1
    num = (pow(10, pos - 1) + (k // pos) - 1)
    if k % pos == 0:
        # print(str(num)[-1])
        pass

    else:
        # print(str(num + (0 if pos == 1 else 1))[(k % pos) - 1])
        pass


# 示例：自动生成一些测试数据并运行
if __name__ == "__main__":
    # 根据规模 n 生成测试：比如从 1 到 n 的多个 k 值
    test_n = 20  # 可根据需要调整规模
    for k in range(1, test_n + 1):
        main(k)