def main(n):
    # n 作为测试规模：构造 q = n 组测试数据
    # 第 t 组数据使用长度为 len(s) = t + 2 的字符串，k = (t % (t + 2)) + 1
    q = n
    sample = "RGB"
    for t in range(1, q + 1):
        length = t + 2
        # 构造一个确定性的字符串 s，长度为 length
        # 字符由 'R', 'G', 'B' 按固定模式生成
        s_chars = []
        for i in range(length):
            s_chars.append(sample[(i * 2 + t) % 3])
        s = "".join(s_chars)
        k = (t % length) + 1

        ans = k
        for i in range(length - k + 1):
            cnt = 0
            x = 0
            for j in range(i, i + k):
                if s[j] != sample[x]:
                    cnt += 1
                x = (x + 1) % 3
            ans = min(ans, cnt)

            cnt = 0
            x = 1
            for j in range(i, i + k):
                if s[j] != sample[x]:
                    cnt += 1
                x = (x + 1) % 3
            ans = min(ans, cnt)

            cnt = 0
            x = 2
            for j in range(i, i + k):
                if s[j] != sample[x]:
                    cnt += 1
                x = (x + 1) % 3
            ans = min(ans, cnt)
        print(ans)


if __name__ == "__main__":
    main(5)