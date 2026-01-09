def main(n):
    # 生成确定性的输入列表，长度为 n，元素在 1..4 之间循环
    l = [i % 4 + 1 for i in range(1, n + 1)]

    s1 = s2 = s3 = s4 = 0
    for i in l:
        if i == 1:
            s1 += 1
        if i == 2:
            s2 += 1
        if i == 3:
            s3 += 1
        if i == 4:
            s4 += 1

    if s3 > 2 or s2 > 1 or s1 > 0 or (s4 == 2 and s2 == 1):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)