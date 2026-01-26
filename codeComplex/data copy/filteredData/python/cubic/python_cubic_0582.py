import sys
import math

def main(n):
    # 生成确定性的 a 和 b，长度都为 n，内容为 0-9 的循环
    a = ''.join(str(i % 10) for i in range(n))
    b = ''.join(str((i * 3 + 1) % 10) for i in range(n))

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
        ans = ''

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)