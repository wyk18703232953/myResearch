import random

def main(n: int):
    # 生成测试数据 l, r（每个位置左/右侧比它大的元素个数）
    # 简单做法：先随机生成一个排列，再根据该排列反推 l, r
    perm = list(range(1, n + 1))
    random.shuffle(perm)

    l = [0] * n
    r = [0] * n
    for i in range(n):
        cl = 0
        cr = 0
        for j in range(i):
            if perm[j] > perm[i]:
                cl += 1
        for j in range(i + 1, n):
            if perm[j] > perm[i]:
                cr += 1
        l[i] = cl
        r[i] = cr

    # 原始逻辑开始（去掉 input，直接使用生成的 l, r）
    flag = True
    ans = [n for _ in range(n)]
    check_l = [0 for _ in range(n)]
    check_r = [0 for _ in range(n)]

    for i in range(n):
        ans[i] -= l[i] + r[i]

    for i in range(n):
        cl, cr = 0, 0
        for j in range(i):
            if ans[j] > ans[i]:
                cl += 1
        for j in range(i + 1, n):
            if ans[j] > ans[i]:
                cr += 1
        if cl != l[i] or cr != r[i]:
            flag = False
            break

    mini = min(ans) - 1
    for i in range(n):
        ans[i] -= mini

    if flag:
        print("YES")
        for v in ans:
            print(v, end=' ')
        print()
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)