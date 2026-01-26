def main(n):
    # 生成确定性字符串列表，长度为 n
    # 第 i 个字符串长度为 i+1，由重复字符模式构成
    ar = []
    base_chars = "abcdefghijklmnopqrstuvwxyz"
    m = len(base_chars)
    for i in range(n):
        length = i + 1
        s = []
        for j in range(length):
            s.append(base_chars[(i + j) % m])
        ar.append("".join(s))

    sortedAr = sorted(ar, key=len)
    flag = False
    for i in range(n - 1):
        if sortedAr[i + 1].find(sortedAr[i]) == -1:
            # print('NO')
            pass
            flag = True
            break
    if not flag:
        # print('YES')
        pass
        for s in sortedAr:
            # print(s)
            pass
if __name__ == "__main__":
    main(5)