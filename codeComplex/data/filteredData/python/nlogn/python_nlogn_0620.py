def main(n: int) -> int:
    """
    根据规模 n 执行原逻辑：
    原始功能：
        ans = sum_{i=2..n} sum_{j=i*2..n, step=i} 4 * (j // i)
    这里直接对传入的 n 计算并返回结果。
    """
    ans = 0
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            ans += 4 * (j // i)
    return ans


if __name__ == "__main__":
    # 根据 n 生成测试数据：此题中 n 即为规模参数，
    # 不需要额外复杂结构，直接调用 main(n) 即可。
    # 这里示例使用 n = 10 作为测试规模。
    test_n = 10
    result = main(test_n)
    # print(result)
    pass