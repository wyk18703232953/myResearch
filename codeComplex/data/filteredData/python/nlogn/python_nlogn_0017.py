def main(n):
    # 生成确定性输入：长度为 n 的整数列表
    # 保证有重复元素，方便测试不同情况
    vals = [(i // 3) for i in range(n)]
    # 模拟原程序逻辑
    vals.sort()
    flag = 0
    for i in vals:
        if i > vals[0]:
            print(i)
            flag = 1
            break
    if flag == 0:
        print('NO')


if __name__ == "__main__":
    main(10)