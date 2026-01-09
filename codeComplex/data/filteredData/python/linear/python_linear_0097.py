def main(n):
    # 生成确定性字符串 s，长度为 n，由小写字母周期性构造
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = len(alphabet)
    s = "".join(alphabet[i % m] for i in range(n))

    p, q, r = len(set(s)), {}, 10**6
    for i in range(n):
        q[s[i]] = i
        if len(q) == p:
            r = min(r, max(q.values()) - min(q.values()))
    # print(r + 1)
    pass
if __name__ == "__main__":
    main(10000)