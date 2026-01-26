def main(n):
    # 将 n 作为原程序中的 n
    s = n // 2  # 规模相关的确定性生成：保证 n > s 在多数情况下成立
    if n <= s:
        # print(0)
        pass
        return
    for i in range(s, n + 2):
        l = 0
        for j in str(i):
            l += int(j)
        if i - l >= s:
            break
    # print(max(n - i + 1, 0))
    pass
if __name__ == "__main__":
    main(10)