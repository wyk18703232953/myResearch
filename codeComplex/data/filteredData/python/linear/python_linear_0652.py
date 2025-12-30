import random

def main(n):
    # 生成测试数据：
    # 固定 c = 1，并生成 n 个在 [1, 10] 范围内的整数作为数组 a
    c = 1
    max_val = 10
    a = [random.randint(1, max_val) for _ in range(n)]

    # 原程序逻辑开始
    f = []
    for _ in range(0, 500001):
        f.append(0)
    l = []
    for _ in range(0, 500001):
        l.append([0])
    m = 0
    for i in range(n):
        l[a[i]].append(f[a[i]] - m)
        if a[i] == c:
            m += 1
        f[a[i]] += 1
        l[a[i]].append(f[a[i]] - m)
    ma = 0
    for i_list in l:
        mi = 0
        for j in i_list:
            if j < mi:
                mi = j
            if ma < j - mi:
                ma = j - mi
    print(m + ma)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)