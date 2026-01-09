def possible(a, index, a1, b):
    rem = []
    for i in range(len(a)):
        if i != index:
            rem.append(a[i])

    a3 = a1[:]
    rem.sort()
    a3.append(a[index])
    a3.extend(rem)
    a2 = ''
    for i in a3:
        a2 += str(i)

    if int(a2) <= b:
        return True

    return False


def main(n):
    # 生成测试数据：
    # a 为长度为 n 的数字列表（例如从 9 递减取模）
    # b 为一个上界整数（这里简单设为由 a 降序组成的整数）
    a = [9 - (i % 10) for i in range(n)]
    # b 设置为尽量大的数：将 a 的降序排列拼成整数
    tmp = sorted(a, reverse=True)
    b_str = ''.join(str(x) for x in tmp)
    b = int(b_str)

    a.sort(reverse=True)
    a1 = []
    pos = 0
    while pos < len(a):
        for i in range(len(a)):
            if possible(a, i, a1, b):
                a1.append(a[i])
                a.pop(i)
                break
        pos += 1

    # 输出结果
    for i in a1:
        # print(i, end='')
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)