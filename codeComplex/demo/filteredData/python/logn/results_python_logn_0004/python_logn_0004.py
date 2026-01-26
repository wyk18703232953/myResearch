def main(n):
    # 在原程序中，只有一组输入 a, b
    # 这里用 n 生成一个确定性的 (a, b)，保持可规模化：
    # a = n, b = 2n + 1
    a = n
    b = 2 * n + 1

    if a == b:
        result = 0

    else:
        x = a ^ b
        c = 0
        while x:
            x //= 2
            c += 1
        result = 2 ** c - 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)