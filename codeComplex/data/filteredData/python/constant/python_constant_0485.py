def main(n):
    # 根据 n 生成测试数据，这里假设令 k = n^2 作为规模相关的测试值
    k = n * n

    s = k // n
    if k % n != 0:
        s += 1
    print(s)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)