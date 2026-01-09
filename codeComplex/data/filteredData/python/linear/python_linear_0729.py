def main(n):
    # 这里根据 n 自动生成 k 的测试数据
    # 可以根据需要修改生成规则，这里示例设定 k = n // 2
    k = n // 2

    chuj_twojej_starej = (n - k) // 2 + 1
    i = 1
    while True:
        if i % chuj_twojej_starej == 0:
            # print(0, end="")
            pass

        else:
            # print(1, end="")
            pass
        if i == n:
            break
        i += 1


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)