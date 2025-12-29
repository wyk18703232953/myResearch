from math import ceil

def main(n: int):
    # 原逻辑：根据第 n 位数字，求出对应的数位并输出该数字
    if n <= 9:
        print(n)
    else:
        d = 2
        ov = 9
        while n > d * 9 * (10 ** (d - 1)) + ov:
            ov = d * 9 * (10 ** (d - 1)) + ov
            d += 1
        v = ceil((n - ov) / d) + int('9' * (d - 1))
        print(str(v)[(n - ov - 1) % d])

if __name__ == "__main__":
    # 这里给一个示例规模 n，可按需修改或在外部调用 main(n)
    test_n = 1000
    main(test_n)