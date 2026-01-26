def main(n):
    # 生成确定性测试数据：长度为 n 的整数序列
    # 这里选择 a[i] = i，为严格递增序列，便于保持原算法逻辑
    a = [i for i in range(n)]

    fl = False
    ans = True
    for i in range(n - 1):
        if a[i + 1] > a[i]:
            if fl:
                ans = False

        else:
            fl = True

    if ans:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模做时间复杂度实验
    main(10)