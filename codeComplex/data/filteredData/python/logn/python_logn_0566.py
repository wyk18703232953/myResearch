def main(n: int):
    # 生成测试数据：这里直接将 n 作为 k 使用
    k = n

    nc = [0 for _ in range(14)]

    for i in range(1, 14):
        nc[i] += nc[i - 1] + 9 * (10 ** (i - 1)) * i

    cif = 0
    for i in range(13):
        if nc[i] < k <= nc[i + 1]:
            cif = i + 1
            break

    if cif == 1:
        print(k)
        return

    c = k - nc[cif - 1]

    if c % cif == 0:
        nnr = c // cif
        ncif = cif
    else:
        nnr = 1 + c // cif
        ncif = c % cif

    number = nnr + 10 ** (cif - 1) - 1

    while cif != ncif:
        number //= 10
        cif -= 1

    print(number % 10)


if __name__ == "__main__":
    # 示例：调用 main(15)，可根据需要修改 n 的值
    main(15)