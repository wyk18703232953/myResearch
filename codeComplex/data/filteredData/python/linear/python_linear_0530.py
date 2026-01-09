def main(n):
    ct = [0] * 26

    # 映射规则：
    # k 在 [1, 26] 之间循环
    if n <= 0:
        k = 1

    else:
        k = (n - 1) % 26 + 1

    # 构造长度为 n 的大写字母字符串 s（确定性）
    # 使用重复字母序列 'A'..'Z'
    chars = []
    for i in range(n):
        chars.append(chr(ord('A') + (i % 26)))
    s = "".join(chars)

    for ch in s:
        ct[ord(ch) - ord('A')] += 1

    result = min(ct[:k]) * k
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)