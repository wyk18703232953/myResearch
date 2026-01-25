def main(n):
    # n 用作字符串长度规模
    if n <= 0:
        return

    # 构造确定性的 T（测试次数）与 k
    # 让 T 与 n 存在线性关系，避免过多循环
    T = 3
    k = max(1, n // 3)

    curr = ['R', 'G', 'B']

    for t in range(T):
        # 构造一个确定性的长度为 n 的字符串 s，循环使用 'R','G','B'
        s = ''.join(curr[(i + t) % 3] for i in range(n))

        a = 10 ** 9
        ans = [[0] * n for _ in range(3)]

        # 计算每种起始偏移 l 的差异数组
        for l in range(3):
            z = l
            for j in range(n):
                if s[j] != curr[z]:
                    ans[l][j] = 1
                z += 1
                z %= 3

        # 前缀和准备：在每行前加一个 0
        for i in range(3):
            ans[i] = [0] + ans[i]

        # 计算前缀和
        for l in range(3):
            for j in range(1, n + 1):
                ans[l][j] += ans[l][j - 1]

        # 枚举所有长度为 k 的子串，计算最小修改次数
        for l in range(3):
            for j in range(1, n - k + 2):
                a = min(a, ans[l][j + k - 1] - ans[l][j - 1])

        print(a)


if __name__ == "__main__":
    main(10)