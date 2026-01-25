def main(n):
    a = []
    for i in range(n + 1):
        a.append(((n + 1) - i) * i)
    print(max(a))


if __name__ == "__main__":
    # 示例：以 10 作为规模参数运行
    main(10)