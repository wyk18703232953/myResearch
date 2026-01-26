import math

def main(n):
    # 根据 n 构造两个只含 '+' 和 '-' 的序列 a, b
    # 保证规模随 n 线性增长，模式完全确定
    length = max(1, n)

    # a: 前半部分 '+', 后半部分 '-'
    a = ['+'] * (length // 2) + ['-'] * (length - length // 2)
    # b: 交替 '+', '-'
    b = ['+' if i % 2 == 0 else '-' for i in range(length)]

    x = a.count('+') - b.count('+')
    y = a.count('-') - b.count('-')

    if x < 0 or y < 0:
        print(0)
    else:
        fact = math.factorial(x + y) / (math.factorial(x) * math.factorial(y))
        total = 2 ** (x + y)
        print(fact / total)

if __name__ == "__main__":
    for n in [1, 5, 10]:
        main(n)