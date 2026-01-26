def main(n):
    # 映射：输入结构为两个整数 n, k
    # 这里将 k 定义为 n // 2，当 n < 2 时特殊处理以避免除零等问题
    if n < 2:
        k = 1

    else:
        k = n // 2

    strr = ""
    # 为避免 (n - k) // 2 变为 0，保证至少为 1
    block_len = (n - k) // 2
    if block_len <= 0:
        block_len = 1

    while len(strr) < n:
        strr += "0" * block_len + "1"
    strr = strr[:n]
    # print(strr)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模进行实验
    main(10)