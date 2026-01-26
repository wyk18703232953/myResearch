def main(n):
    # 生成确定性字符串列表，长度为 n
    # 第 i 个字符串为由 i//3 个 'a'，i//2 个 'b'，以及 i 个 (i % 3) 的字符组成
    s = []
    for i in range(n):
        part1 = 'a' * (i // 3 + 1)
        part2 = 'b' * (i // 2 + 1)
        part3 = str(i % 3) * (i % 5 + 1)
        s.append(part1 + part2 + part3)

    a = sorted(s, key=len)
    c = 1
    for i in range(n - 1):
        if a[i] not in a[i + 1]:
            c = 0
            break
    if c == 0:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
        for i in range(n):
            # print(a[i])
            pass
if __name__ == "__main__":
    main(5)