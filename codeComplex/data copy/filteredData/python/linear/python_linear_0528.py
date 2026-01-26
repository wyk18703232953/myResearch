def main(n):
    # 映射规模参数 n 到原程序的 n 和 k
    # 这里令原始 n = n，k = max(1, min(26, n // 2))
    orig_n = max(1, n)
    k = max(1, min(26, orig_n // 2 if orig_n >= 2 else 1))

    # 构造确定性的字符串 s，长度为 orig_n，字符在 'A' 到 'A'+k-1 之间循环
    letters = [chr(ord('A') + (i % k)) for i in range(orig_n)]
    s = ''.join(letters)

    # 以下是原算法逻辑（去掉所有输入依赖）
    c = [0] * 26
    for i in range(orig_n):
        if s[i] <= chr(ord('A') + k - 1):
            c[ord(s[i]) - ord('A')] += 1
    result = min(c[:k]) * k
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用，可按需要修改 n
    main(10)