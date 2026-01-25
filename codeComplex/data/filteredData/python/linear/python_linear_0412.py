def main(n):
    # n 作为字符串 c 的长度；a 固定为 26，b 固定为 n//2（保证可行）
    a = 26
    b = max(1, min(a // 2, n // 2))
    lis = "abcdefghijklmnopqrstuvwxyz"
    # 构造长度为 n 的字符串 c：循环使用字母表前 a 个字母
    if n <= 0:
        c = ""
    else:
        c = "".join(lis[i % a] for i in range(n))

    su = 0
    cnt = 0
    j = -2
    i = 0
    while i < 26 and cnt < b:
        if lis[i] in c and i - 2 >= j:
            su += i + 1
            cnt += 1
            j = i
        i += 1
    if cnt < b:
        print(-1)
    else:
        print(su)


if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模参数
    main(100)