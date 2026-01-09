def main(n):
    # 确定性数据生成：
    # 将 n 映射为 5 个整数 a,b,x,y,z
    # 规模线性依赖 n，保持值适中方便时间复杂度实验
    a = n
    b = 2 * n
    x = n // 2
    y = n // 3
    z = n // 4

    yel = x * 2 + y
    bul = y + z * 3
    result = max(0, yel - a) + max(0, bul - b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)