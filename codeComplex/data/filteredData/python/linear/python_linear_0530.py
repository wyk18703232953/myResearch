def main(n):
    # 将 n 映射为字符串长度和 k 的大小
    if n < 1:
        n = 1
    k = min(26, max(1, n % 26 or 1))
    length = n

    ct = [0] * 26

    # 确定性生成只包含前 k 个大写字母的字符串
    # 第 i 个字符为 chr(ord('A') + (i % k))
    s = "".join(chr(ord('A') + (i % k)) for i in range(length))

    for ch in s:
        ct[ord(ch) - ord('A')] += 1

    result = min(ct[:k]) * k
    print(result)


if __name__ == "__main__":
    main(100)