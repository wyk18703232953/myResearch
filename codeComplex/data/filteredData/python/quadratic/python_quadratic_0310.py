import math

def main(n):
    # n 表示数组长度，k 为子数组最小长度，确定性构造
    k = max(1, n // 3)  # 至少 1，约为 n/3
    l = [i % 10 for i in range(1, n + 1)]  # 确定性整数序列

    ans = 0.0
    for i in range(n):
        c = 0
        sum1 = 0
        for j in range(i, n):
            sum1 += l[j]
            c += 1
            if c >= k:
                ans = max(ans, sum1 / c)
    print(ans)


if __name__ == "__main__":
    main(10)