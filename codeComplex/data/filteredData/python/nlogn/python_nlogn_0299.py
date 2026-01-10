def main(n):
    # n 表示两座位数量，也是字符串长度
    two_seats = []
    j = 1
    # 生成确定性的两座位权重列表：n, n-1, ..., 1
    for item in range(n, 0, -1):
        two_seats.append((int(item), j))
        j += 1

    two_seats.sort(key=lambda x: -x[0])

    # 生成长度为 n 的01字符串，确定性构造：前半部分 '0'，后半部分 '1'
    s = []
    half = n // 2
    for i in range(n):
        if i < half:
            s.append('0')
        else:
            s.append('1')

    one_seat = []
    res = []
    # 保持原始算法逻辑
    for person in s:
        if person == '0':
            q = two_seats.pop()
            res.append(str(q[1]))
            one_seat.append(q)
        else:
            res.append(str(one_seat.pop()[1]))
    print(" ".join(res))


if __name__ == "__main__":
    main(10)