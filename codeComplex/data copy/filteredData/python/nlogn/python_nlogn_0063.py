def main(n):
    # 生成确定性的输入数据：长度为 n 的整数数组
    # 这里使用从 1 到 n 的递增序列作为示例输入规模
    a = [i for i in range(1, n + 1)]
    
    a.sort()
    total_money = sum(a)
    i_have = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        reaming = total_money - i_have
        if i_have > reaming:
            break
        i_have += a[i]
        cnt += 1
    # print(cnt)
    pass
if __name__ == "__main__":
    main(10)