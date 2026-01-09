def main(n):
    # 输入规模：n 表示数组 A 的长度
    if n < 2:
        # print(0)
        pass
        return

    # 确定性生成数组 A：长度为 n，元素为 i*i + 3*i + 1
    A = [i * i + 3 * i + 1 for i in range(n)]

    k = 10 ** 10
    for i in range(1, n - 1):
        k = min(k, min(A[0], A[i]) // i)
        k = min(k, min(A[-1], A[i]) // (n - i - 1))
    k = min(k, min(A[0], A[-1]) // (n - 1))
    # print(k)
    pass
if __name__ == "__main__":
    main(10)