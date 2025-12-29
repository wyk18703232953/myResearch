def main(n: int):
    k = 1000001
    a = [True] * k
    a[0] = a[1] = False

    for i in range(k):
        if a[i]:
            j = 2 * i
            while j < k:
                a[j] = False
                j += i

    for i in range(4, n):
        if not a[i] and not a[n - i]:
            print(i, n - i)
            return

if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据，这里直接使用 n 本身作为输入
    # 可按需要修改为其他生成规则
    n = 100  # 测试规模
    main(n)