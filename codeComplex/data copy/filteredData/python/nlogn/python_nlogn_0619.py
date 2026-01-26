def main(n: int) -> int:
    # 若需要根据 n 生成测试数据，可在此处扩展。
    # 目前该程序本身只依赖于规模 n，因此直接使用 n 计算结果。
    ans = 0
    j = 2
    # 原代码为 range(2, n/2 + 1)，在 Python3 中需要使用整数除法
    for i in range(2, n // 2 + 1):
        while i * j <= n:
            ans += j * 4
            j += 1

        else:
            j = 2
    return ans


if __name__ == "__main__":
    # 示例：选择一个规模 n 进行测试
    test_n = 100
    # print(main(test_n))
    pass