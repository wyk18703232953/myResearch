import random

def checksq(n: int) -> int:
    m = int(n ** 0.5)
    if m * m == n:
        return m
    m += 1
    if m * m == n:
        return m
    return -1

def solve_one(n: int) -> str:
    if n % 2 == 1:
        return "NO"
    if checksq(n // 2) != -1:
        return "YES"
    n //= 2
    if n % 2 == 1:
        return "NO"
    if checksq(n // 2) != -1:
        return "YES"
    return "NO"

def main(n: int):
    """
    n: 规模参数，用于生成 n 个测试数据并输出对应结果
    """

    # 根据规模 n 生成 n 个测试数据
    # 这里生成的每个测试值为 1 到 4*n 范围内的随机整数
    test_cases = [random.randint(1, 4 * n) for _ in range(n)]

    for value in test_cases:
        print(solve_one(value))

if __name__ == "__main__":
    # 示例：调用 main(5) 生成并判断 5 个测试数据
    main(5)