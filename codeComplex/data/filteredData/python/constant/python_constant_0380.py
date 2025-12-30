import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设 a, b, c 都在 [0, n] 范围内，且 n 为给定规模参数
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, min(a, b, n))  # 一般让 c 不超过 a、b、n 更合理
    # 若希望完全无约束随机，可改成：c = random.randint(0, n)

    result = n - a - b + c
    output = result if result > 0 and c <= a and c <= b else -1
    print(output)

if __name__ == "__main__":
    # 示例：调用 main(100) 作为规模为 100 的测试
    main(100)