def main(n):
    # 构造确定性字符串 s，长度为 n，由 'H' 和 'T' 组成
    # 规则：偶数位置为 'H'，奇数位置为 'T'
    s = ''.join('H' if i % 2 == 0 else 'T' for i in range(n))

    h = s.count('H')
    s2 = s + s
    if h == 0 or h == n:
        # 没有 'H' 或全是 'H'，窗口大小为 0 或 n，结果为 0
        result = 0

    else:
        result = min(s2[i:i + h].count('T') for i in range(n))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)