def main(n):
    # 生成长度为 n 的字符串，周期性包含 'x' 和 'o'
    # 这样既有连续的 'x' 段，又有分隔符，适合作为原算法的输入规模含义
    pattern = ['x', 'x', 'x', 'o']
    x = ''.join(pattern[i % len(pattern)] for i in range(n))

    c = 0
    ans = 0
    for ch in x:
        if ch == 'x':
            c += 1
        else:
            ans += max(0, c - 2)
            c = 0
    ans += max(0, c - 2)
    print(ans)


if __name__ == "__main__":
    main(10)