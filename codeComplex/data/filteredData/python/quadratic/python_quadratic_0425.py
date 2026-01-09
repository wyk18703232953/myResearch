def main(n):
    # 生成确定性的输入：
    # 将 n 作为字符串长度，构造由 0/1/2 组成的字符串
    # 保证每次相同 n 生成的数据一致
    s = ''.join(str((i * 7) % 3) for i in range(n))

    l = []
    total = 0
    p = 0
    for i in range(0, 450):
        sum1 = 0
        flag = 1
        r = 0
        for k in range(n):
            sum1 = sum1 + int(s[k])
            if sum1 > i:
                flag = 0
            if sum1 == i:
                sum1 = 0
                r = r + 1
        if r >= 2 and sum1 == 0 and flag == 1:
            # print("YES")
            pass
            p = 1
            break
    if p == 0:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行规模实验
    main(1000)