def main(n: int) -> int:
    """
    根据规模 n 生成测试数据并返回答案。
    这里的测试数据为 1..n 的整数序列，可按需要自行调整生成方式。
    """

    # 生成测试数据：A 为长度为 n 的整数数组
    A = list(range(1, n + 1))

    A.sort()
    ANS = [0] * n

    NOW = 1
    for i in range(n):
        if ANS[i] == 0:
            ANS[i] = NOW
            # 将与 A[i] 成整除关系的尚未标记的元素都标记为当前组
            for j in range(i, n):
                if A[j] % A[i] == 0 and ANS[j] == 0:
                    ANS[j] = NOW
            NOW += 1

    return max(ANS)


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    print(main(10))