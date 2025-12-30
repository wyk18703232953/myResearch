# Converted version with main(n), no input(), auto-generated test data.

class ADigitsSequenceEasyEdition:
    def solve(self, k: int) -> str:
        # core logic unchanged, but returns the result instead of printing
        k = k + 1
        p = 1
        c = 0
        while c + p * (10 ** p - (10 ** (p - 1) if p > 1 else 0)) < k:
            c += p * (10 ** p - (10 ** (p - 1) if p > 1 else 0))
            p += 1
        k -= c
        bef = (10 ** (p - 1) if p > 1 else 0) + (k - 1) // p
        return str(bef)[(k - 1) % p]


def main(n: int):
    """
    n 为规模参数，这里用作测试数据的大小上界。
    生成测试数据：k = 1, 2, ..., n，分别调用原算法，并将结果按顺序拼接输出。
    可根据需要修改测试数据生成方式。
    """
    solver = ADigitsSequenceEasyEdition()
    # 生成测试数据：1..n
    results = []
    for k in range(1, n + 1):
        results.append(solver.solve(k))
    # 输出结果：一行字符串
    print("".join(results))


if __name__ == "__main__":
    # 示例：使用 n = 20 运行
    main(20)