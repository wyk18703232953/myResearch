def main(n):
    # 确定性生成两个字符串 s1, s2
    # s1 长度为 max(1, n)，s2 固定长度 3
    m = max(1, n)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s1 = "".join(alphabet[i % 26] for i in range(m))
    s2 = "".join(alphabet[(i * 3 + 1) % 26] for i in range(3))

    s1, s2 = s1, s2  # 保留原变量名形式
    ans = s1[0]
    for i in range(1, len(s1)):
        if s1[i] < s2[0]:
            ans += s1[i]
            if i == len(s1) - 1:
                ans += s2[0]
        else:
            ans += s2[0]
            break
    if len(s1) == 1:
        print(s1[0] + s2[0])
    else:
        print(ans)


if __name__ == "__main__":
    main(10)