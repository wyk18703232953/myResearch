def main(n):
    # n 作为字符串长度规模参数
    if n <= 0:
        print(0)
        print(-1, -1)
        return

    # 生成两个确定性的字符串 a 和 b，长度为 n
    # 字符集限制在小写字母，使用简单算术构造
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    a = "".join(chars)
    # b 为 a 经过确定性规则扰动后的结果
    # 规则：将每个字符向后偏移 (i % 3) 位，模 26
    b_chars = []
    for i, ch in enumerate(a):
        offset = i % 3
        base = ord('a')
        new_ch = chr(base + ((ord(ch) - base + offset) % 26))
        b_chars.append(new_ch)
    b = "".join(b_chars)

    num = n
    dic = {}
    lis = []
    ham = 0
    swap1 = -1
    swap2 = -1
    p = False
    q = False

    for i in range(num):
        if a[i] != b[i]:
            ham += 1
            lis.append(i)
            dic[b[i]] = i

    for i in lis:
        if a[i] in dic:
            p = True
            swap1 = i + 1
            f = dic[a[i]]
            swap2 = f + 1
            if a[f] == b[i]:
                q = True
                break

    print(ham - (2 if q else 1 if p else 0))
    print(swap1, swap2)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模参数运行
    main(10)