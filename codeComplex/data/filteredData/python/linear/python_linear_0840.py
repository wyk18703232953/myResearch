def main(n):
    # n 作为测试规模：构造 q=n 组测试数据
    # 第 i 组：长度为 length = i+1，窗口 k = max(1, length//2)
    # 字符串 s 由 'RGB' 周期性构成
    q = n
    ans = []
    for case_idx in range(q):
        length = case_idx + 1
        k = max(1, length // 2)
        base_pattern = "RGB"
        s = "".join(base_pattern[i % 3] for i in range(length))

        min_ans = 10 ** 9
        pr1 = [0]
        pr2 = [0]
        pr3 = [0]

        for i in range(length):
            count1 = 0
            count2 = 0
            count3 = 0
            if i % 3 == 0:
                if s[i] != "R":
                    count1 += 1
                if s[i] != "G":
                    count2 += 1
                if s[i] != "B":
                    count3 += 1
            if i % 3 == 1:
                if s[i] != "G":
                    count1 += 1
                if s[i] != "B":
                    count2 += 1
                if s[i] != "R":
                    count3 += 1
            if i % 3 == 2:
                if s[i] != "B":
                    count1 += 1
                if s[i] != "R":
                    count2 += 1
                if s[i] != "G":
                    count3 += 1
            pr1.append(pr1[-1] + count1)
            pr2.append(pr2[-1] + count2)
            pr3.append(pr3[-1] + count3)
            j = i + 1
            if j >= k:
                c1 = pr1[j] - pr1[j - k]
                c2 = pr2[j] - pr2[j - k]
                c3 = pr3[j] - pr3[j - k]
                if c1 < min_ans:
                    min_ans = c1
                if c2 < min_ans:
                    min_ans = c2
                if c3 < min_ans:
                    min_ans = c3
        ans.append(min_ans)
    # print(*ans, sep="\n")
    pass
if __name__ == "__main__":
    main(10)