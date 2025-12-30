import random

def main(n: int):
    # 1. 生成测试数据
    # 这里根据规模 n 生成 a, b（可按需要调整生成策略）
    # 示例策略：a, b 都是 [0, 2^n - 1] 范围内的随机整数
    if n <= 0:
        a, b = 0, 0
    else:
        upper = (1 << n) - 1
        a = random.randint(0, upper)
        b = random.randint(0, upper)

    # 2. 原始逻辑
    b1 = bin(b)[2:]
    a1 = bin(a)[2:]
    if len(a1) == len(b1):
        d = (b ^ a)
        v = d.bit_length()
        result = int("0" + "1" * v, 2)
    else:
        result = int("1" * len(b1), 2)

    # 3. 输出结果（如需同时查看 a, b 也可一并输出）
    print(result)

if __name__ == "__main__":
    # 示例：运行时给一个固定规模，如 n = 10
    main(10)