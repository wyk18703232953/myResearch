def main(n: int):
    # 预处理：idx[d] = 所有 1~d 位数 一共包含的数字个数
    idx = {0: 0}
    s = 0
    num = 9
    for digit in range(1, 12):
        s += num * digit
        idx[digit] = s
        num *= 10

    N = n  # 使用参数 n 作为要查询的第 N 位

    number = 0
    r = 0
    d = 0
    for digit in range(1, 12):
        if idx[digit - 1] < N <= idx[digit]:
            number = (N - idx[digit - 1]) // digit
            r = (N - idx[digit - 1]) % digit
            d = digit
            break

    if r != 0:
        number += 1

    num = 10 ** (d - 1) + number - 1
    digits = [int(i) for i in str(num)]

    if r == 0:
        print(digits[-1])
    else:
        print(digits[r - 1])


if __name__ == "__main__":
    # 示例：生成规模为 100 的测试，查询第 100 位数字
    main(100)