def main(n):
    # 生成两个确定性的字符串 s1, s2，长度均为 n
    # 字符由 'a' 到 'z' 按照索引循环生成
    if n <= 0:
        print("")
        return

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s1 = "".join(alphabet[i % 26] for i in range(n))
    s2 = "".join(alphabet[(i * 2) % 26] for i in range(n))

    ans = 'z' * 21
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            candidate = s1[:i] + s2[:j]
            if candidate < ans:
                ans = candidate
    print(ans)


if __name__ == "__main__":
    main(10)