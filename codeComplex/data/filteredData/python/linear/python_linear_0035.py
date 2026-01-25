def main(n):
    # 生成长度为 n 的确定性字符串 s，由 'H' 和 'T' 组成
    # 这里用 i % 3 的结果来决定字符，保证可重复且随 n 变化
    base = ''.join('H' if i % 3 == 0 else 'T' for i in range(n))
    s = base * 2

    h = s.count('H') // 2
    if h == 0:
        print(0)
        return

    max_h = 0
    # 滑动窗口计算长度为 h 的子串中 'H' 的最大数量
    current_h = s[:h].count('H')
    max_h = current_h

    for i in range(1, n):
        if s[i - 1] == 'H':
            current_h -= 1
        if s[i + h - 1] == 'H':
            current_h += 1
        if current_h > max_h:
            max_h = current_h

    print(h - max_h)


if __name__ == "__main__":
    # 示例调用，可以根据需要修改 n
    main(10)