def main(n):
    # n 作为规模参数：q = n，且每组测试的字符串长度和 k 也与 n 相关
    q = n
    results = []
    for i in range(q):
        # 为不同测试用例生成确定性的 n_i, k_i
        n_i = max(1, n + i)              # 字符串长度随 i 线性变化
        k_i = max(1, (i % n_i) + 1)      # 保证 1 <= k_i <= n_i
        # 生成由 'R','G','B' 组成的确定性字符串
        chars = ['R', 'G', 'B']
        s = ''.join(chars[(j + i) % 3] for j in range(n_i))

        R = G = B = 0
        ans = float('inf')

        for j in range(n_i):
            if j % 3 == 0:
                if s[j] == 'R':
                    G += 1
                    B += 1
                elif s[j] == 'G':
                    R += 1
                    B += 1
                else:
                    R += 1
                    G += 1
            elif j % 3 == 1:
                if s[j] == 'R':
                    G += 1
                    R += 1
                elif s[j] == 'G':
                    G += 1
                    B += 1
                else:
                    R += 1
                    B += 1
            else:
                if s[j] == 'R':
                    R += 1
                    B += 1
                elif s[j] == 'G':
                    R += 1
                    G += 1
                else:
                    G += 1
                    B += 1

            if j >= k_i - 1:
                if R < ans:
                    ans = R
                if G < ans:
                    ans = G
                if B < ans:
                    ans = B

                idx = j - k_i + 1
                if idx % 3 == 0:
                    if s[idx] == 'R':
                        G -= 1
                        B -= 1
                    elif s[idx] == 'G':
                        R -= 1
                        B -= 1
                    else:
                        R -= 1
                        G -= 1
                elif idx % 3 == 1:
                    if s[idx] == 'R':
                        G -= 1
                        R -= 1
                    elif s[idx] == 'G':
                        G -= 1
                        B -= 1
                    else:
                        R -= 1
                        B -= 1
                else:
                    if s[idx] == 'R':
                        R -= 1
                        B -= 1
                    elif s[idx] == 'G':
                        R -= 1
                        G -= 1
                    else:
                        G -= 1
                        B -= 1

        results.append(ans)

    for v in results:
        print(v)


if __name__ == "__main__":
    main(10)