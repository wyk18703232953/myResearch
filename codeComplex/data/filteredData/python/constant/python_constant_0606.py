def main(n):
    # 映射：将 n 作为原程序中的 n，k 由 n 确定性生成
    # 避免除零，令 k = max(1, n % 10 + 1)，当 n 很大时仍然是 O(1)
    k = max(1, n % 10 + 1)
    ans = (n * 2 + k - 1) // k + (n * 5 + k - 1) // k + (n * 8 + k - 1) // k
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)