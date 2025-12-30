import random

def main(n):
    # 生成一组“合理”的 l, r 和 candies，使得原逻辑必然输出 YES
    # 构造方法：先生成 candies，然后根据定义反推 l, r

    # 1. 生成随机 candies（不要求是排列，只要是整数即可）
    # 为了方便验证，取 0 ~ n 范围内的整数
    candies = [random.randint(0, n) for _ in range(n)]

    # 2. 根据 candies 计算 l, r：
    #    l[i] = 左边有多少 j < i 满足 candies[j] > candies[i]
    #    r[i] = 右边有多少 j > i 满足 candies[j] > candies[i]
    l = [0] * n
    r = [0] * n
    for i in range(n):
        l_cnt = 0
        r_cnt = 0
        for j in range(i):
            if candies[j] > candies[i]:
                l_cnt += 1
        for j in range(i + 1, n):
            if candies[j] > candies[i]:
                r_cnt += 1
        l[i] = l_cnt
        r[i] = r_cnt

    # 以下为原程序逻辑（去掉 input，直接使用生成好的 l, r）

    a = [[l[i] + r[i], i] for i in range(n)]
    a.sort()
    candies_rec = [0 for _ in range(n)]

    if a[0][0] != 0:
        print('NO')
        return

    candies_rec[a[0][1]] = n - a[0][0]

    for i in range(1, n):
        if a[i][0] != a[i - 1][0] and a[i][0] != i:
            print('NO')
            return
        candies_rec[a[i][1]] = n - a[i][0]

    for i in range(n):
        l1 = 0
        r1 = 0
        for j in range(i):
            if candies_rec[j] > candies_rec[i]:
                l1 += 1
        for j in range(i + 1, n):
            if candies_rec[j] > candies_rec[i]:
                r1 += 1
        if l1 != l[i] or r1 != r[i]:
            print('NO')
            return

    print('YES')
    print(*candies_rec)


# 示例：如需运行测试，可调用 main(n)
# main(5)