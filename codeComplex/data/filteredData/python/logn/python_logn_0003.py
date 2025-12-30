import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里假设 l, r 为 [0, 2^n - 1] 范围内的整数（可按需要调整）
    if n <= 0:
        l = r = 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)

    # 原始逻辑
    x = l ^ r
    a = 2
    if l == r:
        print(0)
    else:
        while a <= x:
            a = a * 2
        print(a - 1)

if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模为 5 的测试数据
    main(5)