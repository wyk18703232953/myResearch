def main(n):
    # 确定性生成字符串 s，长度为 n
    # 使用重复的模式来保证有重复子串，便于保留原算法行为
    if n <= 0:
        s = ""

    else:
        base = "abcdefghijklmnopqrstuvwxyz"
        s = "".join(base[i % len(base)] for i in range(n))

    sLen, ans = len(s), 0

    for i in range(sLen):
        for till1 in range(i + 1, sLen + 1):
            till2 = till1 + 1
            for j in range(i + 1, sLen):
                if till2 > sLen:
                    break
                sub1 = s[i:till1]
                sub2 = s[j:till2]
                subLen = len(sub1)
                if sub1 == sub2 and ans < subLen:
                    ans = subLen
                till2 += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)