def prefix_func(s):
    slen, k = len(s), 0
    p = [0] * slen
    p[0] = 0
    for i in range(1, slen):
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

def main(n):
    # 输入规模解释：
    # n: 字符串长度，同时令 k = n 作为重复次数规模
    if n <= 0:
        return ""
    k = n
    # 生成一个确定性的字符串，周期性使用 'a'..'z'
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    l = prefix_func(s)[-1]
    result = s + s[l:] * (k - 1)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)