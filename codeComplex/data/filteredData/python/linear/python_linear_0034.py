def main(n):
    # 生成一个确定性的长度为 n 的字符串 s，由 'H' 和 'T' 构成
    # 规则：索引为 i 的字符为 'H' 当且仅当 (i % 3 == 0 or i % 5 == 0)，否则为 'T'
    s = ''.join('H' if (i % 3 == 0 or i % 5 == 0) else 'T' for i in range(n))

    h = s.count('H')
    if h == 0:
        # 原逻辑中 h 为 0 时窗口长度为 0，切片 s[i:i+0] 为空串，其 'T' 计数为 0
        print(0)
        return

    s2 = s + s
    ans = min(s2[i:i + h].count('T') for i in range(n))
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行一次
    main(10)