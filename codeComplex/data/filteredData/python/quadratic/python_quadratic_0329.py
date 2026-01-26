def main(n):
    # 通过 n 生成确定性的 (n_input, d, k)
    # 映射规则保持简单且可规模化
    # n_input: 原程序中的 n
    # d:      范围 [1, max(1, n_input-1)]
    # k:      范围 [1, min(5, n_input)] 用于控制分支复杂度
    if n <= 0:
        n_input = 1
        d = 1
        k = 1

    else:
        n_input = n + 1  # 让规模整体偏大一点，触发更多分支
        if n_input <= 1:
            d = 1

        else:
            d = (n_input // 2) if (n_input // 2) > 0 else 1
        k = (n % 5) + 1
        if k > n_input:
            k = n_input

    # 以下是原程序逻辑，只是将 input 替换为确定性生成的 n_input, d, k
    n_val = n_input
    d_val = d
    k_val = k

    l = []
    i = 1
    if n_val <= d_val:
        # print("NO")
        pass
    elif k_val == 1:
        if n_val > 2:
            # print("NO")
            pass
        elif n_val == 2:
            # print("YES")
            pass
            # print(1, 2)
            pass

    else:
        n_val += 1
        flag = False
        while i < min(d_val + 1, n_val):
            l.append(str(i) + " " + str(i + 1))
            i += 1
        i += 1
        cnt1 = 0
        cnt2 = 1
        se = [[2, d_val + 1, 1]]
        while cnt1 < cnt2:
            start = se[cnt1][0]
            end = se[cnt1][1]
            mode = se[cnt1][2]
            kk = 3
            while (i < n_val) and (kk <= k_val):
                if i < n_val and not flag:
                    j = start
                    while i < n_val and j < end:
                        if mode == 1:
                            c = min(j - start + 1, end - j)

                        else:
                            c = min(end - j, d_val - end + j)
                        if c > 1:
                            se.append([i, i + c - 1, 2])
                            cnt2 += 1
                        ki = j
                        while i < n_val and c > 0:
                            l.append(str(ki) + " " + str(i))
                            c -= 1
                            ki = i
                            i += 1
                        j += 1

                else:
                    flag = True
                    break
                kk += 1
            cnt1 += 1
        if i < n_val or flag:
            # print("NO")
            pass

        else:
            # print("YES")
            pass
            # print('\n'.join(l))
            pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 以进行规模化实验
    main(10)