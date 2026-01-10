def main(n):
    # 生成确定性的字符串列表，长度为 n
    # 第 i 个字符串长度为 i+1，由重复字符模式构成
    a = []
    for i in range(n):
        # 构造一个简单的周期性字符模式，包含 'a'~'z'
        s = []
        for j in range(i + 1):
            s.append(chr(ord('a') + (j % 26)))
        a.append("".join(s))

    # 按字符串长度排序（与原程序一致）
    a_sorted = sorted(a, key=lambda x: len(x))
    v = all(a_sorted[i] in a_sorted[i + 1] for i in range(n - 1))
    if v:
        print('YES')
        print("\n".join(a_sorted))
    else:
        print('NO')


if __name__ == "__main__":
    main(5)