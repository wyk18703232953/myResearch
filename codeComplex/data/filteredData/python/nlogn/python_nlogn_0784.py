def main(n):
    # 映射：n 作为原程序中的 n，k 取 n//2（保证可扩展且有意义）
    if n <= 1:
        # print(0)
        pass
        return
    k = max(1, n // 2)
    if k > n:
        k = n

    # 构造确定性的 A 数组，长度为 n
    # 示例：A[i] = i * 2
    A = [i * 2 for i in range(n)]

    B = []
    for i in range(1, n):
        B.append(A[i] - A[i - 1])
    B.sort()
    # 原逻辑为 sum(B[:n-k])，需保证 n-k 不为负
    limit = max(0, n - k)
    # print(sum(B[:limit]))
    pass
if __name__ == "__main__":
    main(10)