import random
import math

def is_prime(x):
    if x < 2:
        return False
    return all(x % i for i in range(2, int(x ** 0.5) + 1))

def generate_composite_even(n):
    # 生成一个不超过 n 的偶合数
    while True:
        # 保证是偶数，范围 [4, n] 且为偶数
        t = random.randrange(4, n + 1, 2)
        if not is_prime(t):
            return t

def main(n):
    # n 为规模参数，用于控制生成的测试数据范围
    t = generate_composite_even(n)

    for i in range(4, t // 2 + 1):
        if not is_prime(i) and not is_prime(t - i):
            print(i, t - i)
            break

if __name__ == "__main__":
    # 示例：可根据需要修改 n 的大小
    main(1000)