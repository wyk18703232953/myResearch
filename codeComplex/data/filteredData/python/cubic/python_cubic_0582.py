def main(n):
    import random

    # 生成测试数据 a, b
    # a 为长度为 n 的数字字符串，首位不为 0
    # b 为长度为 n 或 n+1 的数字字符串（随机）
    if n <= 0:
        print("")
        return

    # 生成 a
    first_digit = str(random.randint(1, 9))
    rest_digits = ''.join(str(random.randint(0, 9)) for _ in range(n - 1))
    a = first_digit + rest_digits

    # 随机决定 b 的长度为 n 或 n+1
    if random.choice([True, False]):
        len_b = n
    else:
        len_b = n + 1

    # 生成 b（可为任意数字字符串，不保证与 a 有任何关系）
    first_digit_b = str(random.randint(1, 9))
    rest_digits_b = ''.join(str(random.randint(0, 9)) for _ in range(len_b - 1))
    b = first_digit_b + rest_digits_b

    # 以下为原逻辑，仅将 input() 替换为使用生成的 a, b
    dp = [0] * 11
    for ch in a:
        dp[int(ch)] += 1

    if len(b) > len(a):
        ans = ''
        for _ in range(len(a)):
            for j in range(9, -1, -1):
                if dp[j] != 0:
                    ans += str(j)
                    dp[j] -= 1
                    break
    elif len(a) == len(b):
        ans = ''
        a1 = []
        cmpr = ''
        i = 0
        while i < len(a):
            cmpr += b[i]
            if i == 0:
                flag = 0
                for j in range(9, 0, -1):
                    if ans + str(j) <= cmpr and dp[j] != 0:
                        flag = 1
                        dp[j] -= 1
                        ans += str(j)
                        a1.append(j)
                        break
                if flag == 0:
                    dp[1] -= 1
                    a1.append(1)
                    ans += '1'
            else:
                flag = 0
                for j in range(9, -1, -1):
                    if ans + str(j) <= cmpr and dp[j] != 0:
                        flag = 1
                        ans += str(j)
                        a1.append(j)
                        dp[j] -= 1
                        break

                if flag == 0:
                    ch_flag = 0
                    for i1 in range(i - 1, -1, -1):
                        if ch_flag == 1:
                            break
                        for j1 in range(int(ans[i1]) - 1, -1, -1):
                            if i1 == 0:
                                if j1 > 0 and dp[j1] != 0:
                                    dp[a1[i1]] += 1
                                    dp[j1] -= 1
                                    index = i1
                                    a1.pop()
                                    a1.append(j1)
                                    ch_flag = 1
                                    break
                            else:
                                if dp[j1] != 0:
                                    dp[a1[i1]] += 1
                                    dp[j1] -= 1
                                    a1.pop()
                                    index = i1
                                    a1.append(j1)
                                    ch_flag = 1
                                    break
                            if ch_flag == 1:
                                break
                        if ch_flag == 1:
                            break
                        val = a1.pop()
                        dp[val] += 1

                    ans = ''
                    cmpr = ''
                    dp = [0] * 11
                    for i1 in range(len(a)):
                        dp[int(a[i1])] += 1
                    for i1 in range(len(a1)):
                        dp[a1[i1]] -= 1

                    for i1 in range(len(a1)):
                        ans += str(a1[i1])
                        cmpr += b[i1]
                    i = index
            i += 1
    else:
        # 原代码未处理 len(b) < len(a) 的情况，这里与原逻辑保持一致。
        ans = ''

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)