def main(n):
    # 生成确定性的测试数据：长度为 n 的整数数组
    # 这里选择让数组中大部分为奇数，且恰好 1 个偶数或多个偶数，以测试两种分支
    # 规则：arr[i] = 2 * i + 1 为奇数；每第 k 个位置改成偶数
    if n <= 0:
        return
    k = 3  # 控制偶数分布的周期
    arr = []
    for i in range(n):
        val = 2 * i + 1
        if i % k == 0:
            val = 2 * i  # 偶数
        arr.append(val)

    codd = 0
    ceven = 0
    ptodd = -1
    pteven = -1
    for i in range(n):
        if arr[i] % 2 == 0:
            ceven += 1
            pteven = i

        else:
            codd += 1
            ptodd = i

    if ceven == 1:
        # print(pteven + 1)
        pass

    else:
        # print(ptodd + 1)
        pass
if __name__ == "__main__":
    main(10)