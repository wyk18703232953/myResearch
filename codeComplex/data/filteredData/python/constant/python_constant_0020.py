import random

def f(n):
    return n + n // 2

def main(n):
    # 这里根据规模 n 生成一个测试数据 x
    # 示例：生成 [1, n] 范围内的随机整数
    x = random.randint(1, max(1, n))
    print(f(x))

if __name__ == "__main__":
    # 示例：调用 main，规模可以按需调整
    main(10)