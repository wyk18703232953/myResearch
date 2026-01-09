def main(n):
    # 将 n 映射为输入规模
    # A, B, x, y, z 按照与 n 相关的确定性方式生成
    A = 3 * n + 5
    B = 4 * n + 7
    x = n
    y = n // 2
    z = n % 10

    nA = 2 * x + y
    nB = 3 * z + y
    r = 0
    if nA > A:
        r += nA - A
    if nB > B:
        r += nB - B
    # print(r)
    pass
if __name__ == "__main__":
    main(10)