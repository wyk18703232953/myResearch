import random

def has(x, bit):
    return x & (1 << bit)

def solve(l, r):
    bit = 62
    while bit >= 0 and has(l, bit) == has(r, bit):
        bit -= 1
    return (1 << (bit + 1)) - 1 if bit >= 0 else 0

def main(n):
    """
    n: 控制测试数据规模，生成 n 对 (l, r) 并逐个求解。
    这里简单生成：
        l 在 [0, 10^12)
        r 在 [l, l + 10^6] 内，避免 r 过小或乱序。
    """
    random.seed(0)
    results = []
    for _ in range(n):
        l = random.randint(0, 10**12)
        r = l + random.randint(0, 10**6)
        results.append(solve(l, r))
    # 输出所有结果，每行一个
    for v in results:
        print(v)

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)