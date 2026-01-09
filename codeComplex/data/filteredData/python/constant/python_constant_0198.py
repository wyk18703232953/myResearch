def main(n):
    # n 表示列表长度
    # 生成确定性整数列表
    l = [(i * 2 + 3) % (n + 3) + 1 for i in range(n)]
    l = sorted(l)

    if len(l) >= 3 and (
        min(l) == 1 or
        (l[0] == 3 and l[1] == 3 and l[2] == 3) or
        (l[0] == 2 and l[1] == 4 and l[2] == 4) or
        (l[0] == 2 and l[1] == 2)
    ):
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(5)