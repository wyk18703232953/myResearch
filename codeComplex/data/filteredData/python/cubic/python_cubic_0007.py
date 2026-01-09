def main(n):
    # 生成确定性字符串 S，长度为 n
    # 使用周期性模式方便控制规模：例如周期为 3 的 'abc'
    base = "abc"
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
    # 示例调用，可根据需要修改 n 的大小进行时间复杂度实验
    main(1000)