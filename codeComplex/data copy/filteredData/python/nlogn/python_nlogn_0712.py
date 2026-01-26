def main(n):
    # 生成确定性输入：长度为 n 的整数列表 x
    # 示例构造：x[i] = i // 2，确保有重复且随 n 有规模变化
    x = [i // 2 for i in range(n)]

    x.sort()
    count, count2 = 0, 0
    ans = 1
    for i in range(n):
        count += x[i] - i
        if i >= 2 and x[i] == x[i - 1] == x[i - 2]:
            ans = 0
        if i >= 2 and x[i] == x[i - 1] == x[i - 2] + 1:
            ans = 0
        if i >= 1 and x[i] == x[i - 1]:
            count2 += 1
    if n >= 3 and x[0] == x[1] == 0:
        ans = 0
    for i in range(n):
        if x[i] > 0:
            break
        if i == n - 1:
            ans = 0
    if ans == 0 or count % 2 == 0 or count2 > 1:
        # print("cslnb")
        pass

    else:
        # print("sjfnb")
        pass
if __name__ == "__main__":
    main(10)