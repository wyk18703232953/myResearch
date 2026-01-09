def main(n):
    # 解释输入结构：
    # 原程序：a, b = map(int, input().split())
    # 为了可规模化，将 n 映射为：
    # a = n + 1  (避免 a 为 0)
    # b = n * (n + 1)
    a = n + 1
    b = n * (n + 1)
    result = (b + a - 1) // a
    # print(result)
    pass
if __name__ == "__main__":
    main(10)