import random

def fun(k, li, t):
    tem = []
    count = 0
    for i in li:
        if i[0] >= k:
            tem.append(i)
            count += 1
    if count >= k:
        ans = 0
        for i in range(k):
            ans += tem[i][1]
        if ans <= t:
            return True
        else:
            return False
    else:
        return False

def main(n):
    # 生成测试数据：
    # n: 任务数量
    # 每个任务: [ai, ti, index]
    # ai: 能参与的最大学生数 (1..n)
    # ti: 完成所需时间 (1..10^4)
    # t: 总时间限制，为了让有解的概率大些，设置为任务时间和的一半左右
    li = []
    for idx in range(n):
        a = random.randint(1, n)
        time = random.randint(1, 10_000)
        li.append([a, time, idx])

    t = sum(x[1] for x in li) // 2 + 1  # 生成一个相对合理的时间上限

    # 按原代码逻辑进行排序和二分
    li.sort(key=lambda x: x[1])
    l = 0
    r = n
    while r - l > 1:
        mid = (l + r) // 2
        if fun(mid, li, t):
            l = mid
        else:
            r = mid

    fin = 0
    for i in range(l, r + 1):
        if fun(i, li, t):
            fin = i

    print(fin)
    print(fin)
    tem = []
    for i in range(n):
        if li[i][0] >= fin:
            tem.append(li[i][2] + 1)
    print(*tem[:fin])


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次规模为 10 的测试
    main(10)