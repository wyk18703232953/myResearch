def main(n: int):
    # 生成测试数据：将 n 作为“目标第 n 位”，无需实际构造字符串
    # 直接使用原逻辑，但去掉 input()，并确保为整数运算
    n = int(n)
    i = 0
    while True:
        block = 9 * (10 ** i) * (i + 1)
        if n - block <= 0:
            break
        n -= block
        i += 1

    a = n // (i + 1)
    b = n % (i + 1)
    if b != 0:
        print(str(10 ** i + a)[b - 1])
    else:
        print(str(10 ** i + a - 1)[-1])


# 示例调用
if __name__ == "__main__":
    # 比如计算第 1000 位
    main(1000)