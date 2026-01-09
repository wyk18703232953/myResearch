def main(n):
    # n 作为字符串长度，k 作为窗口长度（取 n//2，至少为1）
    if n <= 0:
        return
    q = 5  # 固定 5 组测试用例，保证可规模化、可重复
    results = []
    for t in range(q):
        length = n + t  # 每组长度略有不同，规模仍由 n 控制
        k = max(1, length // 2)
        # 生成确定性的字符串 s，周期为 'R', 'G', 'B'
        pattern = ['R', 'G', 'B']
        s = ''.join(pattern[i % 3] for i in range(length))

        m = 10 ** 4
        for j in range(length):
            if j + k <= length:
                l1 = ["R", "G", "B"]
                m1, m2, m3 = 0, 0, 0
                for i in range(j, j + k):
                    if l1[(i - j) % 3] != s[i]:
                        m1 += 1
                for i in range(j, j + k):
                    if l1[(i + 1 - j) % 3] != s[i]:
                        m2 += 1
                for i in range(j, j + k):
                    if l1[(i + 2 - j) % 3] != s[i]:
                        m3 += 1
                m = min(m, m1, m2, m3)

            else:
                break
        results.append(m)
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)