def main(n):
    # 将 n 解释为字符串长度，同时设置 q 和每个测试的 k
    q = n if n > 0 else 1
    results = []

    for case in range(q):
        # 对于每个测试用例，确定性生成 n 和 k
        cur_n = n
        if cur_n <= 0:
            cur_n = 1
        k = case % cur_n + 1  # 1 <= k <= n

        # 生成确定性字符串 s，长度为 cur_n，由 'R','G','B' 构成
        # 使用简单算术构造：i % 3
        chars = ['R', 'G', 'B']
        s = ''.join(chars[i % 3] for i in range(cur_n))

        R = G = B = 0
        ans = float('inf')

        for j in range(cur_n):
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

            if j >= k - 1:
                ans = min(ans, R, G, B)
                start = j - k + 1
                if start % 3 == 0:
                    if s[start] == 'R':
                        G -= 1
                        B -= 1
                    elif s[start] == 'G':
                        R -= 1
                        B -= 1
                    else:
                        R -= 1
                        G -= 1
                elif start % 3 == 1:
                    if s[start] == 'R':
                        G -= 1
                        R -= 1
                    elif s[start] == 'G':
                        G -= 1
                        B -= 1
                    else:
                        R -= 1
                        B -= 1
                else:
                    if s[start] == 'R':
                        R -= 1
                        B -= 1
                    elif s[start] == 'G':
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