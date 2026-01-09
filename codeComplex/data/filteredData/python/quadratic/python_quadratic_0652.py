def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 这里选择从 1 到 n 的顺序整数
    a = list(range(1, n + 1))

    a.sort()
    ans = 0
    while len(a) > 0:
        k = a.pop(0)
        a = [i for i in a if i % k != 0]
        ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)