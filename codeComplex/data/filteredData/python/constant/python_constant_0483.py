def main(n):
    # 在原始代码中，输入包含两个整数 n 和 k
    # 这里的 n 作为规模参数，对应原程序中的 n
    # 需要确定性生成 k，这里设为 k = n * (n + 1) // 2
    k = n * (n + 1) // 2
    p = (k - 1) // n + 1
    return p

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    result = main(10)
    # print(result)
    pass