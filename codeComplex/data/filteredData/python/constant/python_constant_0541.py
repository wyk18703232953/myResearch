def main(n):
    # 根据规模 n 生成测试数据 s，这里简单设为 s = n*(n+1)//2
    s = n * (n + 1) // 2

    x = s // n
    if x * n < s:
        x += 1
    # print(x)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)