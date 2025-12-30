import random

INF = 10001
mod = int(1e9) + 7

def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素取值 1..5
    a = [random.randint(1, 5) for _ in range(n)]

    # dp1[l][r]: 区间 [l, r] 能整体变为某个值的“层数”，不可则为 0
    # dp3[l][r]: 区间 [l, r] 最少分成多少段，每段都能被“完全压缩”成一个值
    dp1 = [[-1] * n for _ in range(n)]
    dp3 = [[INF] * n for _ in range(n)]

    def cal(l, r):
        if l == r:
            dp1[l][r] = a[l]
            dp3[l][r] = 1
            return dp1[l][r]
        if dp1[l][r] != -1:
            return dp1[l][r]
        for i in range(l, r):
            if cal(l, i) == cal(i + 1, r) != 0:
                dp1[l][r] = dp1[l][i] + 1
                dp3[l][r] = 1
            dp3[l][r] = min(dp3[l][r], dp3[l][i] + dp3[i + 1][r])
        if dp1[l][r] == -1:
            dp1[l][r] = 0
        return dp1[l][r]

    cal(0, n - 1)
    # 返回结果，原代码是输出 dp3[0][n-1]
    return dp3[0][n - 1]


if __name__ == "__main__":
    # 示例：调用 main(5)
    res = main(5)
    print(res)