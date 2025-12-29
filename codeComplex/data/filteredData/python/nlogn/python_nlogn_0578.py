def main(n):
    i = 1
    first = True
    while n:
        if not first:
            print(' ', end='')
        first = False

        if n == 3:
            print(i, i, i * 3, end='')
            break

        print(' '.join([str(i)] * ((n + 1) // 2)), end='')
        i <<= 1
        n >>= 1
    print()


if __name__ == "__main__":
    # 示例：根据需要修改 n 进行测试
    test_n = 10
    main(test_n)