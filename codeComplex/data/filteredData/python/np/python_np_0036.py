def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main(n):
    # 1. 生成长度为 n 的 commands：随机由 '+' 和 '-' 组成
    # 这里简单生成一半 '+' 一半 '-'，不足的补 '+'
    plus_count_cmd = n // 2
    minus_count_cmd = n - plus_count_cmd
    commands = '+' * plus_count_cmd + '-' * minus_count_cmd

    # 2. 生成长度为 n 的 received：
    # 前 1/3 用 '+', 中间 1/3 用 '-', 剩下用 '?'
    one_third = n // 3
    two_third = 2 * n // 3
    received = (
        '+' * one_third +
        '-' * (two_third - one_third) +
        '?' * (n - two_third)
    )

    positive = 0
    negative = 0
    count = 0
    for i in range(n):
        if commands[i] == "+":
            positive += 1
        else:
            negative += 1
        if received[i] == "+":
            positive -= 1
        elif received[i] == "-":
            negative -= 1
        else:
            count += 1

    cases = 2 ** count
    probability = 0.0
    if positive >= 0 and negative >= 0:
        probability = (factorial(count) / (factorial(positive) * factorial(negative))) / cases

    print("{0:.9f}".format(probability))


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要修改
    main(10)