def main(n):
    # 生成确定性的字符串列表，长度从 1 到 n
    # 第 i 个字符串为由字符 'a'+(i%26) 重复 (i % (n//2+1) + 1) 次再加上索引信息
    # 保证有不同长度和内容用于保持算法逻辑
    strings = []
    for i in range(n):
        base_char = chr(ord('a') + (i % 26))
        repeat_len = i % (n // 2 + 1) + 1
        s = base_char * repeat_len + str(i)
        strings.append(s)

    l = strings
    l.sort(key=lambda x: len(x))

    ok = True
    for i in range(n - 1):
        if l[i] not in l[i + 1]:
            ok = False
            break

    if ok:
        print("YES")
        print(*l, sep='\n')
    else:
        print("NO")


if __name__ == "__main__":
    main(10)