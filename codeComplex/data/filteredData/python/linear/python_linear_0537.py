import random

def main(n):
    # 生成规模为 n 的测试数据：包含正数、负数和零
    # 这里生成 [-10, 10] 范围内的随机整数
    a = [random.randint(-10, 10) for _ in range(n)]

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
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)