def main(n):
    # 这里按照题意自行生成 k，示例中简单设为 k = n
    k = n

    d = int((9 + 8 * (n + k)) ** 0.5)
    x = (d - 3) // 2
    # print(n - x)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)