def main(n):
    # 将原来的 n, k 输入结构映射为：
    # n: 输入规模
    # k: 由 n 确定性生成
    k = n + 1 if n > 0 else 1

    a = [2, 5, 8]
    s = 0
    for i in a:
        s += (n * i - 1) // k + 1
    # print(s)
    pass
if __name__ == "__main__":
    main(10)