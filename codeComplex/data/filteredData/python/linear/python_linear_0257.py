def palin(s):
    if s[::-1] != s or len(s) == 0:
        return len(s)

    else:
        return palin(s[1:])

def main(n):
    # 生成一个确定性的字符串，长度为 n
    # 字符构造方式为周期性 'a' 到 'z'
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    result = palin(s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)