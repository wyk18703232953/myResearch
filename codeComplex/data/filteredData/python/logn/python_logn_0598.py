def main(n):
    # 根据 n 生成测试数据 a，这里示例为 a = n 的平方
    # 可以根据需要调整生成规则
    a = n * n

    deb = 1
    fin = n + 1
    while fin - deb > 1:
        m = (fin + deb) // 2
        if (m * (m + 1)) // 2 - (n - m) > a:
            fin = m
        else:
            deb = m
    print(n - deb)


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)