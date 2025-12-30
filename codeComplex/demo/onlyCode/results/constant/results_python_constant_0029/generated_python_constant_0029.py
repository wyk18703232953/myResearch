# Codeforces A. Toy Army
# Converted to use main(n) with generated test data instead of input()

def main(n: int) -> int:
    """
    逻辑封装函数：
    给定规模 n，返回 3 * n / 2 的整数结果。
    """
    return int(3 * n / 2)

if __name__ == "__main__":
    # 根据 n 生成测试数据，这里示例：从 1 到 10 的若干 n
    test_ns = [1, 2, 3, 4, 5, 10]
    for n in test_ns:
        result = main(n)
        print(f"n = {n}, answer = {result}")