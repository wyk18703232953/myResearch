def main(n: int):
    # 生成测试数据：随机生成 m（虽然原代码未使用 m，这里保留结构）
    # 为了简单，可令 m = n 的某个函数或固定值，这里设为 n 本身
    m = n  # 占位变量，保持与原程序接口一致，但不参与计算

    a = 1
    for _ in range(n - 1):
        a *= 10
        a += 1
    b = 10 ** n - a

    print(a)
    print(b)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)