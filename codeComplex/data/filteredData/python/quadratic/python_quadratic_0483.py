import random


def main(n: int):
    # 生成满足条件的测试数据 l, r, k
    # 随机生成一个长度为 n 的排列 k（元素范围 1..n）
    k = list(range(1, n + 1))
    random.shuffle(k)

    # 根据原程序逻辑反推 l, r
    l = []
    r = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(0, i):
            if k[j] > k[i]:
                c += 1
        for j in range(i + 1, n):
            if k[j] > k[i]:
                d += 1
        l.append(c)
        r.append(d)

    # 按原程序逻辑进行校验
    if l[0] != 0 or r[n - 1] != 0:
        print("NO")
        return

    s = [(l[i] + r[i]) for i in range(n)]
    m = max(s) + 1
    k_recovered = [m - x for x in s]

    l1 = []
    r1 = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(0, i):
            if k_recovered[j] > k_recovered[i]:
                c += 1
        for j in range(i + 1, n):
            if k_recovered[j] > k_recovered[i]:
                d += 1
        l1.append(c)
        r1.append(d)

    if l1 != l or r1 != r:
        print("NO")
    else:
        print("YES")
        print(*k_recovered)


# 示例调用
if __name__ == "__main__":
    main(5)