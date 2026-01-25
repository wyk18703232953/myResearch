def main(n):
    # 确定性生成输入数据
    p = n + 1 if n > 0 else 1
    list1 = [(i * 2 + 3) % (p * 3 + 7) for i in range(n)]

    mx = 0
    curr = 0
    nxt = sum(list1)
    for i in range(n - 1):
        curr += list1[i]
        nxt -= list1[i]
        mx = max(mx, curr % p + nxt % p)
    print(mx)


if __name__ == "__main__":
    main(10)