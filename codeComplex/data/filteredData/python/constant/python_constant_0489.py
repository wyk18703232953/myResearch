def main(n):
    # 将 n 映射为原程序中的 a, b
    # 保证 a >= 1，b >= 1，且随 n 规模线性增长
    a = max(1, n)
    b = n * n + n  # 简单确定性构造
    result = (b + a - 1) // a
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做规模实验
    main(10)