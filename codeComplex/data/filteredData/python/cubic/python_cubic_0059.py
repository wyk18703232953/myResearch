def main(n):
    # 构造确定性字符串 S，长度为 n
    # 这里使用周期模式，保证有重复子串以便算法有意义
    if n <= 0:
        # print(0)
        pass
        return
    base = "abcd"
    S = "".join(base[i % len(base)] for i in range(n))

    best = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            s = S[i:j]
            c = 0
            for k in range(len(S)):
                if S[k:].startswith(s):
                    c += 1
            if c >= 2:
                best = max(best, len(s))
    # print(best)
    pass
if __name__ == "__main__":
    # 示例：以 n=20 作为输入规模
    main(20)