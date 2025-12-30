import random

def main(n):
    # 生成测试数据：长度为 n 的正整数数组
    # 这里生成 1~5 的随机整数，你可以按需要调整范围
    li = [random.randint(1, 5) for _ in range(n)]

    dp1 = [[-1] * n for _ in range(n)]
    dp2 = [0] * n

    for i in range(n):
        dp1[i][i] = li[i]
        dp2[i] = i + 1

    size = 2
    while size <= n:
        i = 0
        while i < n - size + 1:
            j = i + size - 1
            k = i
            while k < j:
                if dp1[i][k] != -1 and dp1[i][k] == dp1[k + 1][j]:
                    dp1[i][j] = dp1[i][k] + 1
                k += 1
            i += 1
        size += 1

    i = 0
    while i < n:
        k = 0
        while k <= i:
            if dp1[k][i] != -1:
                if k == 0:
                    dp2[i] = 1
                else:
                    dp2[i] = min(dp2[i], dp2[k - 1] + 1)
            k += 1
        i += 1

    print(dp2[n - 1])

# 示例调用
# main(5)