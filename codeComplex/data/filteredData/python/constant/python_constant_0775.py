from math import sqrt
import random

def main(n):
    """
    n: 测试数据规模（测试用例个数）
    根据 n 随机生成 n 个整数，每个整数在 [1, 10**9] 范围内，
    并对每个整数按原逻辑输出 YES/NO。
    """
    # 生成测试数据
    test_cases = [random.randint(1, 10**9) for _ in range(n)]

    # 处理逻辑
    for value in test_cases:
        half = value / 2
        quarter = value / 4
        cond1 = int(sqrt(half)) == sqrt(half)
        cond2 = int(sqrt(quarter)) == sqrt(quarter)
        if cond1 or cond2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)