def main(n):
    # 映射：原程序中 n 为字符串长度，k 为字母种类数
    # 这里令 k = min(26, max(1, n % 26 + 1))，保证 1 <= k <= 26
    k = min(26, max(1, n % 26 + 1))

    # 生成确定性字符串：循环使用前 k 个大写字母，长度为 n
    # 对应原程序的第二次 input()
    s = ''.join(chr(ord('A') + (i % k)) for i in range(n))

    count = [0] * k
    for c in s:
        idx = ord(c) - ord("A")
        if 0 <= idx < k:
            count[idx] += 1

    # 为保证与原逻辑兼容（count 长度为 k，索引 0..k-1）
    # 若 k > 实际使用字母数，也没问题，因为我们只生成前 k 个字母
    result = k * min(count)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)