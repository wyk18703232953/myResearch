def main(n):
    # n 控制字符串长度和 num
    num = n
    # 构造两个确定性的字符串 a 和 b，长度为 num
    # 使用小写字母周期模式
    letters = "abcdefghijklmnopqrstuvwxyz"
    a = "".join(letters[i % 26] for i in range(num))
    # b 是 a 的一个确定性变换：每个字符向后偏移 1（循环）
    b = "".join(letters[(i + 1) % 26] for i in range(num))

    dic = {}
    lis = []
    ham = 0
    swap1 = -1
    swap2 = -1
    p = False
    q = False

    for i in range(num):
        if a[i] != b[i]:
            ham += 1
            lis.append(i)
            dic[b[i]] = i

    for i in lis:
        if a[i] in dic:
            p = True
            swap1 = i + 1
            f = dic[a[i]]
            swap2 = f + 1
            if a[f] == b[i]:
                q = True
                break

    # print(ham - (2 if q else 1 if p else 0))
    pass
    # print(swap1, swap2)
    pass
if __name__ == "__main__":
    # 示例：用规模 n=10 运行一次
    main(10)