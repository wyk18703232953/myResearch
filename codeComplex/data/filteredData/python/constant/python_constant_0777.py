import random

def chk(n: int) -> bool:
    return int(n ** 0.5 + 0.1) ** 2 == n

def solve_one(n: int) -> str:
    if (n % 2 == 0 and chk(n // 2)) or (n % 4 == 0 and chk(n // 4)):
        return "YES"
    else:
        return "NO"

def main(n: int):
    """
    n: 测试数据规模，表示生成 n 个随机测试样例并输出结果。
    每个样例是一个正整数，范围可按需调整。
    """
    # 生成 n 个测试数据，这里选取 1~10^9 范围内的随机整数
    test_cases = [random.randint(1, 10**9) for _ in range(n)]

    for x in test_cases:
        print(solve_one(x))

if __name__ == "__main__":
    # 示例：运行时可在此处指定规模
    main(10)