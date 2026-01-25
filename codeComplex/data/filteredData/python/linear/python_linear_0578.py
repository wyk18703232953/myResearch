def main(n):
    res = []
    multiplier = 1
    while n > 1:
        new_n = n // 2
        res.extend((multiplier,) * (n - new_n))
        if n == 3:
            multiplier *= 3
        else:
            multiplier *= 2
        n = new_n
    res.extend((multiplier,) * n)
    print(*res)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)