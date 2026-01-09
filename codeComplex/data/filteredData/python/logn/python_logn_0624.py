def main(n):
    # 将 n 作为原程序中的 n，k 从 n 映射得到，保证确定性
    k = n // 2
    val = int((2 * n + 3 - (8 * n + 8 * k + 9) ** (1 / 2)) // 2)
    # print(val)
    pass
if __name__ == "__main__":
    main(10)