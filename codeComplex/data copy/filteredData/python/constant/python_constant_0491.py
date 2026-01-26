def main(n):
    # 在原程序中，输入为两个整数 n 和 k
    # 这里将 n 视为第一个整数，第二个整数 k 由 n 确定性生成
    # 例如设定 k = n * n
    k = n * n
    result = (k + n - 1) // n
    # print(result)
    pass
if __name__ == "__main__":
    main(10)