def main(n: int):
    mult = 1
    res = []
    remain = n
    while remain > 0:
        if remain == 2:
            res.extend([mult, mult * 2])
            remain = 0
        elif remain == 3:
            res.extend([mult, mult, mult * 3])
            remain = 0
        else:
            half = remain // 2
            extra = remain - half
            res.extend([mult] * extra)
            remain = half
            mult = mult * 2
    print(*res)


if __name__ == "__main__":
    # 示例：根据需要修改 n 的值进行测试
    n = 10
    main(n)