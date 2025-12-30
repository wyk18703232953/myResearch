def main(n: int):
    # 根据规模 n 生成测试数据：
    # a 为 n，比特长度大致为 n 的大小数量级；b 比 a 大至少 1
    # 为避免 n 太小或为 0 的情况，进行简单处理
    if n <= 1:
        a = 1
        b = 2
    else:
        a = n
        b = n * 2 + 1

    # 原逻辑开始
    a, b = min(a, b), max(a, b)
    A = bin(a)[2:]
    B = bin(b)[2:]
    A = "0" * (len(B) - len(A)) + A
    diff = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            diff = len(A) - i
            break
    print((2 ** diff) - 1)


if __name__ == "__main__":
    # 举例：调用 main(10)
    main(10)