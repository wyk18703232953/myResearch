s = ""

def main(n):
    global s
    # 生成一个确定性的字符串，长度为 n
    # 使用重复的模式来保证存在重复子串，便于保持原算法行为有意义
    base = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = "".join(base)

    mc = -1
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for cu in range(len(s) - max(i, j)):
                if s[i + cu] == s[j + cu]:
                    if cu > mc:
                        mc = cu

                else:
                    break
    # print(mc + 1)
    pass
if __name__ == "__main__":
    main(10)