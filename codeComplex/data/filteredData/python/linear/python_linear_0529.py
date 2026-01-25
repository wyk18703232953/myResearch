def main(n):
    # 生成确定性输入：
    # k = min(n, 26)，保证字母不超过 'A' 到 'Z'
    k = n if n <= 26 else 26
    if k <= 0:
        print(0)
        return

    # 生成长度为 n 的字符串 s，由前 k 个大写字母循环构成
    # 如 n=7,k=3 -> "ABCABCA"
    letters = [chr(ord('A') + i) for i in range(k)]
    s = ''.join(letters[i % k] for i in range(n))

    m = 10 ** 10
    for i in range(k):
        c = chr(ord('A') + i)
        m = min(m, s.count(c))
    print(m * k)


if __name__ == "__main__":
    main(10)