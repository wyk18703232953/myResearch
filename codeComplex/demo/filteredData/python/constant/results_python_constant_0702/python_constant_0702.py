def main(n):
    # 生成确定性输入：n 和 v
    # 将原程序中的 n 固定为传入的 n，将 v 设为 n//2，保证规模关系随 n 变化
    v = n // 2

    if n < v + 2:
        result = n - 1

    else:
        result = int(v - 1 + (n - v) * (n - v + 1) / 2)

    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行时间复杂度实验
    main(10)