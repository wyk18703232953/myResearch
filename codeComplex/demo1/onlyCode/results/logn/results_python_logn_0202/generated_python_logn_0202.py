def main(n):
    # 生成测试数据：将 s 设置为 n 的字符串形式
    s = str(n)

    i = int(s)
    d_sum = sum(map(int, str(i)))
    while i - d_sum < int(s):
        i += 1
        d_sum = sum(map(int, str(i)))

    # 输出结果
    print(max(0, int(n) - i + 1))


if __name__ == "__main__":
    # 可以在这里修改测试规模 n
    main(100)