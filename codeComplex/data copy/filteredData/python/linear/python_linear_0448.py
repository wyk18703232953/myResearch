def main(n):
    # 生成确定性的 m, a, b
    # 让 m 在 [max(1, n-2), n+2] 范围内变化，保证可扩展
    m = max(1, n - 2) + (n % 5)

    # 为了可扩展性，我们让 a 和 b 的长度与 n、m 相关
    # a 的长度为 n，b 的长度为 m
    # 在 a 中放一个 '*'，位置由 n 确定（若 n>1）
    if n <= 0:
        a = ""

    else:
        star_pos = n // 2  # 确定性位置
        a_chars = []
        for i in range(n):
            if i == star_pos:
                a_chars.append('*')

            else:
                # 生成一些确定性的字母模式
                a_chars.append(chr(ord('a') + (i % 3)))
        a = "".join(a_chars)

    if m <= 0:
        b = ""

    else:
        # 根据 m 构造 b，与 a 有部分相似但又有区分，便于复杂度实验
        b_chars = []
        for i in range(m):
            # 通过 i 和 n 的组合产生确定性的模式
            base = (i + n) % 4
            if base == 0:
                b_chars.append('a')
            elif base == 1:
                b_chars.append('b')
            elif base == 2:
                b_chars.append('c')

            else:
                b_chars.append('d')
        b = "".join(b_chars)

    # 原程序核心逻辑
    if '*' in a:
        c = a.replace('*', '')
        i = a.index('*')
        if c == b:
            # print("YES")
            pass
        elif a[:i] == b[:i]:
            t = a[i + 1:]
            tt = b[m - len(a) + 1 + i:]
            if t == tt and len(a) - 1 <= m:
                # print("YES")
                pass

            else:
                # print("NO")
                pass

        else:
            # print("NO")
            pass
    elif len(a) > m:
        # print("NO")
        pass

    else:
        if a == b:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    # 示例调用，可自行调整 n
    main(10)