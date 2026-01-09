def main(n):
    # 生成确定性输入：长度为 n 的整数列表
    # 构造方式：重复序列 [0, 1, 2, 0, 1, 2, ...] 长度为 n
    l1 = [i % 3 for i in range(n)]

    if len(set(l1)) == 1 and l1[0] > 0:
        # print(1)
        pass

    else:
        l2 = list(set(l1))
        x = l1.count(0)
        if x == 0:
            # print(len(l2))
            pass

        else:
            # print(len(l2) - 1)
            pass
if __name__ == "__main__":
    main(10)