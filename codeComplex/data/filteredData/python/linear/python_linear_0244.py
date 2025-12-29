import random
import string

def ct(s):
    a = [0] * (26 * 2)
    for i in s:
        if 'A' <= i <= 'Z':
            a[ord(i) - 65] += 1
        elif 'a' <= i <= 'z':
            a[ord(i) - 97 + 26] += 1
    return max(a)

def generate_string(length):
    # 生成由大小写字母组成的随机字符串
    chars = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(chars) for _ in range(length))

def main(n):
    # 规模 n 用于控制字符串长度
    # 这里设计为：
    # 长度 ln = max(1, n)   （避免 ln 为 0）
    ln = max(1, n)

    # 生成三条测试数据
    s1_raw = generate_string(ln)
    s2_raw = generate_string(ln)
    s3_raw = generate_string(ln)

    # 保留原始逻辑
    s1 = ct(s1_raw)
    s2 = ct(s2_raw)
    s3 = ct(s3_raw)
    s = [s1, s2, s3]

    for i in range(len(s)):
        if s[i] == ln and n == 1:
            s[i] = ln - 1
        else:
            s[i] = s[i] + n
        if s[i] > ln:
            s[i] = ln

    s1, s2, s3 = s[0], s[1], s[2]
    s.sort()

    if s[2] == s[1]:
        print('Draw')
    elif s[-1] == s1:
        print('Kuro')
    elif s[-1] == s2:
        print('Shiro')
    elif s[-1] == s3:
        print('Katie')


if __name__ == "__main__":
    # 示例：规模设为 5，可按需修改或在外部调用 main(n)
    main(5)