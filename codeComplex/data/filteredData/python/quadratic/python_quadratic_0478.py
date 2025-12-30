import random

def main(n):
    # 生成一个随机的 CANDIES 排名 1..n 的排列
    CANDIES = list(range(1, n + 1))
    random.shuffle(CANDIES)

    # 根据 CANDIES 计算 l 和 r
    l = [0] * n
    r = [0] * n
    for i in range(n):
        lc = 0
        rc = 0
        for j in range(i):
            if CANDIES[j] > CANDIES[i]:
                lc += 1
        for j in range(i + 1, n):
            if CANDIES[j] > CANDIES[i]:
                rc += 1
        l[i] = lc
        r[i] = rc

    # 原逻辑开始（去掉 input，改用生成的 l, r）
    cost = [(l[i] + r[i], i) for i in range(n)]
    cost.sort()

    res = [None] * n
    res[cost[0][1]] = n

    candy = n
    for i in range(1, n):
        if cost[i][0] == cost[i - 1][0]:
            res[cost[i][1]] = candy
        else:
            candy -= 1
            res[cost[i][1]] = candy

    check = 1
    for i in range(n):
        lc = 0
        rc = 0
        for j in range(i):
            if res[j] > res[i]:
                lc += 1
        for j in range(i + 1, n):
            if res[j] > res[i]:
                rc += 1
        if lc != l[i] or rc != r[i]:
            check = 0

    if check == 1:
        print("YES")
        for c in res:
            print(c, end=" ")
        print()
    else:
        print("NO")

# 示例调用：
# main(5)