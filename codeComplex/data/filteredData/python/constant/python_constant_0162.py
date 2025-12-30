def main(n):
    # 1. 根据 n 设定筛的上界（原程序是固定 1000001，这里随 n 调整）
    # 为了安全起见，上界至少要 > n
    k = max(1000001, n + 1)

    # 2. 构建埃拉托斯特尼筛，a[x] 为 True 表示 x 是素数
    a = [True] * k
    a[0] = a[1] = False

    for i in range(2, int(k ** 0.5) + 1):
        if a[i]:
            for j in range(i * i, k, i):
                a[j] = False

    # 3. 查找分解：原逻辑是找 i 使得 i 和 n-i 都为合数
    for i in range(4, n):
        if not a[i] and not a[n - i]:
            print(i, n - i)
            return

if __name__ == "__main__":
    # 示例：自动生成一个测试规模 n
    # 可以根据需要修改生成规则
    test_n = 100  # 示例：固定一个 n，或改为任意正偶数等
    main(test_n)