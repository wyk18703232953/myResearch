def main(n):
    # 将 n 拆为原程序的 n 和 k，并确定性生成字符串 s
    # 这里：原_n = n，k = max(1, n // 3)，s 为长度原_n 的周期字符串
    original_n = n
    k = max(1, n // 3)
    if original_n <= 0:
        # print("")
        pass
        return

    base = "abc"
    s = "".join(base[i % len(base)] for i in range(original_n))

    # 原始逻辑开始
    n_val = original_n
    flag = True
    lenn = 10**10
    ans = ""
    for i in range(n_val):
        s1 = s + s[n_val - i - 1:] * (k - 1)
        cnt = 0
        for j in range(len(s1) - len(s) + 1):
            if s1[j:j + len(s)] == s:
                cnt += 1
        if cnt == k and len(s1) < lenn:
            ans = s1
            lenn = len(s1)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)