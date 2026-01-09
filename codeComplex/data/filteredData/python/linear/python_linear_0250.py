def main(n):
    # 映射：原程序中的 n、k
    # 使用输入规模 n 作为原 n，k 设为 n*n//4，保证随规模增长
    orig_n = max(3, n)  # 至少为 3，避免过小规模影响结构
    k = (orig_n * orig_n) // 4

    s = [["."] * orig_n for _ in range(4)]
    if k % 2 == 0:
        for j in range(1, orig_n - 1):
            if k == 0:
                break
            s[1][j] = "#"
            s[2][j] = "#"
            k -= 2

    else:
        cen = orig_n // 2
        s[1][cen] = "#"
        k -= 1
        for i in range(1, 3):
            for j in range(1, cen):
                if k > 0:
                    k -= 2
                    s[i][j] = s[i][-j - 1] = "#"

    if k == 0:
        # print("YES")
        pass
        for i in range(4):
            # print("".join(s[i]))
            pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 进行规模实验
    main(10)