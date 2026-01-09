def main(n):
    # 原程序输入结构：两个整数 n, k
    # 这里将规模参数 n 作为原程序中的 n
    # 并构造确定性的 k，用于可规模化实验
    original_n = n
    k = n * n + n  # 确定性构造 k

    ans = k // original_n
    if k % original_n:
        ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)