def main(n):
    # 生成两个确定性的字符串 s1, s2
    # s1 的长度为 n（至少为 1）
    if n <= 0:
        n = 1
    letters = "abcdefghijklmnopqrstuvwxyz"
    m = len(letters)
    s1 = "".join(letters[i % m] for i in range(n))
    s2 = letters[(n * 7) % m] + letters[(n * 13) % m]

    s1, s2 = s1, s2
    ans = s1[0]
    for i in range(1, len(s1)):
        if s1[i] < s2[0]:
            ans += s1[i]

        else:
            break
    result = ans + s2[0]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)