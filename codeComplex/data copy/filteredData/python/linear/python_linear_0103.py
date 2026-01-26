import bisect

def main(n):
    # 根据 n 构造两个字符串 a 和 b，长度分别为 n 和 n//2（至少为 1）
    if n <= 0:
        n = 1
    a_len = n
    b_len = max(1, n // 2)

    # 构造确定性的字符串，字符从 'a' 开始循环
    a = ''.join(chr(ord('a') + (i % 26)) for i in range(a_len))
    b = ''.join(chr(ord('a') + ((i * 7) % 26)) for i in range(b_len))

    p = []
    for i in range(len(a)):
        for j in range(len(b)):
            ok = a[:i+1] + b[:j+1]
            p.append(ok)
    # print(min(p))
    pass
if __name__ == "__main__":
    main(10)