def main(n):
    # 根据 n 构造确定性输入
    # 字符串由前 min(n, 26) 个小写字母按顺序重复构成，长度为 n
    letters = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = "".join(letters)
    # b 设为一个随 n 增长的整数上界，保证为正且规模随 n 变化
    b = int("".join(str((i % 10)) for i in range(1, min(n + 1, 18)))) or 10

    a = sorted(s)
    a = a[::-1]

    p = ""
    while a:
        for i, z in enumerate(a):
            candidate = p + a[i] + "".join(sorted(a[:i] + a[i + 1 :]))
            if int(candidate) <= b:
                p += z
                a.pop(i)
                break

    print(p)


if __name__ == "__main__":
    main(10)