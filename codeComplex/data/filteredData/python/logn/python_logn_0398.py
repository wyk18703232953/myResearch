def main(n: int):
    # 根据规模 n 生成测试数据，这里假设直接使用 n 作为算法输入规模
    # 若需要更复杂的生成方式，可在此调整 n 的赋值逻辑

    i = 0
    ANS = []
    while n > 0:
        if n == 3:
            ANS = ANS + [2 ** i, 2 ** i, 3 * (2 ** i)]
            break
        x = (n + 1) // 2
        ANS = ANS + [2 ** i] * x
        n = n - x
        i += 1

    for a in ANS:
        # print(a, end=" ")
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)