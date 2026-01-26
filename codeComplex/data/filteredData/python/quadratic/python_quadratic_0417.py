tam, q = 10, 5

def main(n):
    # 将 n 映射为 tam、q，保证规模随 n 增长
    # tam 至少为 1，q 至少为 1
    tam = max(1, n)
    q = max(1, n // 2 if n > 1 else 1)

    # 构造确定性字符串 t，长度为 tam
    # 使用小写字母循环：'a'...'z'
    t = ''.join(chr(ord('a') + (i % 26)) for i in range(tam))
    s = t

    posi = -1
    for j in range(tam - 1):
        if t[:j + 1] == t[tam - j - 1:]:
            posi = j

    add = t[posi + 1:]

    for _ in range(q - 1):
        s += add

    # print(s)
    pass
if __name__ == "__main__":
    main(10)