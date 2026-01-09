def main(n):
    M = 998244353

    # 生成确定性输入数据：长度为 n 的整数数组 a
    # 这里选择 a[i] = (i * 3 + 1) % M 作为确定性构造
    a = [(i * 3 + 1) % M for i in range(n)]

    series = [1]
    fact = 1
    for i in range(n + 1):
        series.append(((series[-1] * 2) % M + fact) % M)
        fact = (fact * 2) % M

    ind = n - 1
    ans = 0

    for i in range(n):
        ans = (ans + (a[i] * series[ind]) % M) % M
        ind -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小进行实验
    main(10)