def prefix_func(s):
    slen, k = len(s), 0
    p = [0] * slen
    if slen == 0:
        return p
    p[0] = 0
    for i in range(1, slen):
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

def main(n):
    if n < 1:
        n = 1
    # 生成字符串长度和重复次数
    s_len = n
    k = n
    # 确定性构造字符串：周期为 26 的小写字母序列
    base = [chr(ord('a') + (i % 26)) for i in range(s_len)]
    s = "".join(base)
    l = prefix_func(s)[-1] if s_len > 0 else 0
    result = s + s[l:] * (k - 1)
    print(result)

if __name__ == "__main__":
    main(5)