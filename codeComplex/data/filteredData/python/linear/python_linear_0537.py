def main(n):
    if n <= 0:
        return
    # 生成长度为 n 的整数数组 a，包含正数、负数和零，且模式确定
    # a[i] = (i // 3) * (-1 if i % 2 else 1)
    a = [(i // 3) * (-1 if i % 2 else 1) for i in range(n)]

    if n == 1:
        print(a[0])
    else:
        prod_minus = False
        for i in range(n - 1):
            if a[i] * a[i + 1] <= 0:
                prod_minus = True
                break
        Min_abs = float("inf")
        Sum = 0
        for num in a:
            Sum += abs(num)
            if abs(num) < Min_abs:
                Min_abs = abs(num)

        if prod_minus:
            print(Sum)
        else:
            print(Sum - 2 * Min_abs)


if __name__ == "__main__":
    # 示例：运行若干不同规模
    for size in [1, 5, 10, 1000]:
        main(size)