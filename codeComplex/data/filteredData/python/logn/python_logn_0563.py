import math
import random

def get_digit(x, pos):
    s = []
    while x > 0:
        s.append(x % 10)
        x //= 10
    return s[::-1][pos]

def find_digit(x):
    n = 0
    next_ = 9 * (10 ** n) * (n + 1)

    while next_ <= x:
        x -= next_
        n += 1
        next_ = 9 * (10 ** n) * (n + 1)

    if x == 0:
        return 9

    pos_ = 10 ** n + math.ceil(x / (n + 1)) - 1
    return get_digit(pos_, (x - 1) % (n + 1))

def main(n):
    # 生成规模为 n 的测试数据，这里假设 k 的取值范围是 [1, n]
    if n < 1:
        return
    k = random.randint(1, n)
    print(find_digit(k))

if __name__ == "__main__":
    # 示例：用某个规模参数调用 main
    main(1000)