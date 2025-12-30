def main(n: int):
    # 将原程序中的 k 输入替换为由规模 n 生成的测试数据
    # 这里简单设定测试数据 k = n（可根据需要自行调整生成规则）
    k = n
    k -= 1

    pow_10, length = 1, 1

    while 9 * pow_10 * length < k:
        k -= 9 * pow_10 * length
        pow_10 *= 10
        length += 1

    div = k // length
    rem = k % length

    num = pow_10 + div

    print(str(num)[rem])


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)