def main(n):
    # n 表示数组 b 的长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的数组 b
    # 这里使用一个简单的算术构造：b[i] = (i * 3) % (n + 5) + i
    b = [(i * 3) % (n + 5) + i for i in range(n)]

    a1 = [0]
    a2 = [b[0]]

    for x in b[1:]:
        new_a = a1[-1]
        if x - new_a > a2[-1]:
            new_a = x - a2[-1]
        new_a2 = x - new_a
        a1.append(new_a)
        a2.append(new_a2)

    # print(*(a1 + a2[::-1]))
    pass
if __name__ == "__main__":
    main(10)