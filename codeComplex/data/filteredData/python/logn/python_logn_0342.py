def main(n):
    # 这里根据 n 生成测试数据
    # 原程序是从输入读取 n, k，这里我们根据 n 构造一个 k
    # 示例：令 k = n（可按需修改生成方式）
    k = n

    k = k + 1
    z = 1000000007
    c = (n * pow(2, k, z) - pow(2, k - 1, z) + 1) % z

    if n == 0:
        result = 0
    else:
        result = c

    # 按原程序的行为打印结果
    print(result)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行测试
    main(10)