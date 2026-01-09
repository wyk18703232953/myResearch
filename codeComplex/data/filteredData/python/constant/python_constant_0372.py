def main(n):
    # 构造长度为4的整数列表 lis，n 控制数值规模
    lis = [
        n,
        n // 2,
        n // 3,
        n // 4
    ]

    if lis[2] <= lis[0] and lis[2] <= lis[1]:
        if ((lis[0] + lis[1]) - lis[2]) < lis[3]:
            # print(lis[3] - ((lis[0] + lis[1]) - lis[2]))
            pass
        elif sum(lis) == 0:
            # print(-1)
            pass
        elif lis[0] == 0 and lis[1] == 0 and lis[2] == 0:
            # print(lis[3])
            pass

        else:
            # print(-1)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)