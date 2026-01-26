def main(n):
    # 根据规模 n 生成测试数据，这里示例：k = n 的一半向上取整
    # 你可以按需要修改生成方式
    k = (n + 1) // 2

    if k - n >= n:
        # print(0)
        pass
        return

    if k <= n:
        if k % 2:
            # print(k // 2)
            pass

        else:
            # print(k // 2 - 1)
            pass

    else:
        # print(n - k // 2)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)