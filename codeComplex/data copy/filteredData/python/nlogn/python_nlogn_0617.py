def main(n: int) -> int:
    """
    规模 n 作为参数，返回原程序的计算结果。
    这里将“生成测试数据”理解为：直接使用给定的 n 作为原程序中的 n。
    """
    ans = 0
    # 原逻辑：n 从输入读取，这里用参数 n
    for i in range(2, n):
        for j in range(2 * i, n + 1, i):
            ans += j // i
    return ans * 4


# 示例：在本文件中简单测试
if __name__ == "__main__":
    # 你可以在这里自定义 n 的测试值
    test_n = 10
    # print(main(test_n))
    pass