import random

def main(n: int):
    # 生成测试数据：在合理范围内生成一个正整数 counter
    # 这里假设 n 表示 counter 的最大值规模
    # 当 n < 1 时，默认使用 1；否则从 1 到 n 中随机取一个数
    if n < 1:
        counter = 1
    else:
        counter = random.randint(1, n)

    max_counter = 9
    digits_per_number = 1

    while max_counter < counter:
        digits_per_number += 1
        max_counter = max_counter + digits_per_number * 9 * 10 ** (digits_per_number - 1)

    max_real_number = int(str(9) * digits_per_number)
    dif = max_counter - counter
    rem = dif % digits_per_number
    real_number = max_real_number - dif // digits_per_number
    print(str(real_number)[-1 - rem])


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要调整
    main(1000)