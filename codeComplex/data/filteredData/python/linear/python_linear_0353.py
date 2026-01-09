def main(n):
    # 将原本的 (n, m) 输入结构映射为 (n, m=n)
    # 原程序只使用 n，不使用 m
    m = n
    c = 0
    ans = []
    for _ in range(n):
        c ^= 1
        ans.append(str(c))
    ans = "".join(ans)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)