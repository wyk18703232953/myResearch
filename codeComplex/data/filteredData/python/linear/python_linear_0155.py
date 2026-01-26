def main(n):
    # 生成确定性的输入规模和参数 p
    if n <= 0:
        n = 1
    p = n + 7

    # 生成确定性数组 list1，长度为 n
    list1 = [(i * 3 + 5) % (p + 3) for i in range(n)]

    mx = 0
    curr = 0
    nxt = sum(list1)
    for i in range(n - 1):
        curr += list1[i]
        nxt -= list1[i]
        mx = max(mx, curr % p + nxt % p)
    # print(mx)
    pass
if __name__ == "__main__":
    main(10)