def main(n):
    dul = 0
    # 生成确定性的 k，使得既能覆盖 k==0 又能覆盖 k!=0 的分支
    # 这里令 k = n % 3，n 的不同取值会生成不同 k，但完全确定
    k = n % 3
    sum1 = 0

    if k == 0:
        for i in range(n - 1, -1, -1):
            sum1 = sum1 + 1
            dul = dul + sum1
            if dul == i:
                # print(i)
                pass
                break

    if k != 0:
        for i in range(n - 1, -1, -1):
            sum1 = sum1 + 1
            dul = dul + sum1
            if dul - i == k:
                # print(i)
                pass
                break


if __name__ == "__main__":
    main(10)