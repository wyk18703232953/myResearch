def main(n):
    # 生成确定性字符串，长度为 n
    # 使用重复模式 'abc' 构造
    base = "abc"
    s = "".join(base[i % 3] for i in range(n))
    n_len = len(s)
    Ans = 0
    for i in range(n_len):
        for j in range(i + 1, n_len):
            L = i
            R = j
            while L < R and s[L] == s[R]:
                L += 1
                R -= 1
            if L < R and Ans < j - i + 1:
                Ans = j - i + 1
    # print(Ans)
    pass
if __name__ == "__main__":
    main(1000)