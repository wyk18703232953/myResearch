import random

M = 998244353

def main(n):
    # 1. 生成测试数据：长度为 n 的数组 a，元素在 [0, M-1] 内
    a = [random.randrange(M) for _ in range(n)]

    # 2. 原逻辑计算
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

    print(ans)
    return ans, a  # 若只需输出结果，可去掉 a

if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)