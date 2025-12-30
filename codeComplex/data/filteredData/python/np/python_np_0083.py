from math import factorial
import random

def C(m, n):
    return factorial(n) // (factorial(m) * factorial(n - m))

def main(n):
    # 根据规模 n 生成测试数据：
    # command_1: 长度为 n，由 '+' 和 '-' 随机组成
    # command_2: 长度为 n，由 '+', '-', '?' 随机组成
    choices_cmd1 = ['+', '-']
    choices_cmd2 = ['+', '-', '?']

    command_1 = ''.join(random.choice(choices_cmd1) for _ in range(n))
    command_2 = ''.join(random.choice(choices_cmd2) for _ in range(n))

    num = command_2.count('?')
    i = (command_1.count('+') - command_1.count('-') -
         command_2.count('+') + command_2.count('-') + num)

    if i % 2 == 0 and 0 <= i // 2 <= num:
        print("{:.9f}".format(C(i // 2, num) / 2 ** num))
    else:
        print("0.000000000")

if __name__ == "__main__":
    # 示例：使用规模 n = 10 运行
    main(10)