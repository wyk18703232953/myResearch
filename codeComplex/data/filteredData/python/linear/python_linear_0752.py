def main(n):
    # 生成确定性的测试数据：长度为 n 的整数数组
    # 这里生成一个包含正负交替、大小线性变化的序列
    A = [i if i % 2 == 0 else -i for i in range(1, n + 1)]

    if n == 1:
        if A[0] >= 0:
            print(A[0])
        else:
            print(-A[0] - 1)
        return

    for i in range(n):
        if A[i] < 0:
            pass
        else:
            A[i] = -A[i] - 1

    if n % 2 == 0:
        print(*A)
        return

    mim = 0
    indmim = 0
    for i in range(n):
        if A[i] < mim:
            mim = A[i]
            indmim = i
    A[indmim] = -A[indmim] - 1
    print(*A)


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次运行
    main(10)