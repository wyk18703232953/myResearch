import random

def main(n):
    # 生成测试数据 ar，长度为 n
    # 这里简单生成一个随机数组，元素范围可按需调整
    if n <= 0:
        return
    ar = [random.randint(1, 100) for _ in range(n)]

    # 原始逻辑开始
    if n == 1:
        print(1)
        return

    if ar[1] > ar[0]:
        li = [1]
    elif ar[1] < ar[0]:
        li = [5]
    else:
        li = [3]

    c = 1
    while c != n:
        j = 0

        if ar[c] > ar[c - 1]:
            while c != n and ar[c] > ar[c - 1]:
                c += 1
                j += 1
            for _ in range(j - 1):
                li.append(li[-1] + 1)
                if li[-1] == 6:
                    print(-1)
                    return
            if c != n and ar[c] == ar[c - 1]:
                li.append(li[-1] + 1)
            else:
                li.append(5)

        elif ar[c] < ar[c - 1]:
            while c != n and ar[c] < ar[c - 1]:
                c += 1
                j += 1
            for _ in range(j - 1):
                li.append(li[-1] - 1)
                if li[-1] == 0:
                    print(-1)
                    return
            if c != n and ar[c] == ar[c - 1]:
                li.append(li[-1] - 1)
            else:
                li.append(1)

        else:
            while c != n and ar[c] == ar[c - 1]:
                c += 1
                j += 1
            for _ in range(j):
                if li[-1] > 3:
                    li.append(li[-1] - 1)
                else:
                    li.append(li[-1] + 1)
            if c != n and ar[c] > ar[c - 1]:
                if li[-2] == 1:
                    li[-1] = 2
                else:
                    li[-1] = 1
            elif c != n and ar[c] < ar[c - 1]:
                if li[-2] == 5:
                    li[-1] = 4
                else:
                    li[-1] = 5

    if max(li) > 5 or min(li) < 1:
        print(-1)
    else:
        print(*li)


# 示例调用（提交时可移除或保留，按需求）：
# main(5)