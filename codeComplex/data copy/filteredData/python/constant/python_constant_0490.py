def main(n):
    # 在原题中，n 和 k 都是输入。
    # 这里将 n 作为第一个参数，k 由 n 确定性生成，使规模随 n 增长。
    # 例如设 k = n^2，保证是确定性的。
    k = n * n
    result = k // n + (k % n != 0)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)