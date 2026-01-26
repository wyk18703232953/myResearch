def main(n):
    # 生成确定性输入：长度为 n 的整数数组 a
    # 这里选用 a[i] = i // 2，使存在重复元素，覆盖各类分支
    a = [i // 2 for i in range(n)]

    summ = 0
    a.sort()
    if len(a) == 1:
        if a[0] % 2 == 1:
            # print('sjfnb')
            pass

        else:
            # print('cslnb')
            pass
    elif a[0] == a[1] == 0:
        # print('cslnb')
        pass

    else:
        x = False
        for i in range(2, n):
            if a[i] == a[i - 1] and a[i - 1] == a[i - 2]:
                x = True
        if x:
            # print('cslnb')
            pass

        else:
            x = False
            for i in range(2, n):
                if a[i] == a[i - 1] and a[i] - 1 == a[i - 2]:
                    x = True
            if x:
                # print('cslnb')
                pass

            else:
                summ = 0
                for i in range(1, n):
                    if a[i] == a[i - 1]:
                        summ += 1
                if summ > 1:
                    # print('cslnb')
                    pass

                else:
                    summ = 0
                    for i in range(n):
                        summ += a[i] - i
                    if summ % 2 == 0:
                        # print('cslnb')
                        pass

                    else:
                        # print('sjfnb')
                        pass
if __name__ == "__main__":
    main(10)