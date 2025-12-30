import random

def main(n):
    # 生成测试数据 l, r，使之有较大概率可行
    # 生成一个随机答案数组 ans（1..n），然后根据 ans 反推 l, r
    ans = [random.randint(1, n) for _ in range(n)]
    l = [0] * n
    r = [0] * n
    for i in range(n):
        k = 0
        for j in range(i):
            if ans[j] > ans[i]:
                k += 1
        l[i] = k
        k = 0
        for j in range(i + 1, n):
            if ans[j] > ans[i]:
                k += 1
        r[i] = k

    # 下面是原逻辑的封装
    s = [l[i] + r[i] for i in range(n)]
    order = [i for i in range(n)]
    ans_check = [1 for _ in range(n)]

    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if s[m] < s[j]:
                m = j
        t = s[i]
        s[i] = s[m]
        s[m] = t
        t = order[i]
        order[i] = order[m]
        order[m] = t

    cur = 1
    for i in range(1, n):
        if s[i - 1] > s[i]:
            cur += 1
        ans_check[order[i]] = cur

    for i in range(n):
        k = 0
        for j in range(i):
            if ans_check[j] > ans_check[i]:
                k += 1
        if l[i] != k:
            print('NO')
            return
        k = 0
        for j in range(i + 1, n):
            if ans_check[j] > ans_check[i]:
                k += 1
        if r[i] != k:
            print('NO')
            return

    print('YES')
    for x in ans_check:
        print(x, end=' ')

# 示例：直接运行时给个默认规模
if __name__ == "__main__":
    main(5)