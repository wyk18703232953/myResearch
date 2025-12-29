def main(n):
    # 这里根据规模 n 自动生成测试数据 (n, k)
    # 为了体现不同情况，令 k 在 [1, 2n] 之间取一个值
    # 示例：令 k = n + 1（可按需要修改为其它生成规则）
    k = n + 1

    if n >= k:
        result = (k - 1) // 2
    elif n * 2 > k:
        result = n - k // 2
    else:
        result = 0

    print(result)


if __name__ == "__main__":
    # 示例调用：可在此处修改 n 的值进行测试
    main(10)