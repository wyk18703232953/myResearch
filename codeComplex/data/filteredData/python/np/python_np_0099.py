import math
import random

def main(n: int):
    # 生成长度为 n 的字符串 a 和 b，字符只包含 '+' 和 '-'
    # 这样与原逻辑一致（原逻辑只关心 '+' 和 '-' 的计数差）
    choices = ['+', '-']
    a = [random.choice(choices) for _ in range(n)]
    b = [random.choice(choices) for _ in range(n)]

    x = a.count('+') - b.count('+')
    y = a.count('-') - b.count('-')

    if x < 0 or y < 0:
        print(0)
    else:
        fact = math.factorial(x + y) / (math.factorial(x) * math.factorial(y))
        total = 2 ** (x + y)
        print(fact / total)


if __name__ == "__main__":
    # 示例：规模 n 可在此处修改
    main(10)