import random


def main(n):
    # 生成测试数据：随机生成满足非负约束的 l, r
    # 这里简单生成 [0, n-1] 范围内的整数作为示例
    l = [random.randint(0, n - 1) for _ in range(n)]
    r = [random.randint(0, n - 1) for _ in range(n)]

    def update(l, r, i, res):
        j = 0
        # 左侧更新 r
        while j < i:
            if res[j] is None:
                r[j] -= 1
                if r[j] < 0:
                    return False
            j += 1
        j += 1
        # 右侧更新 l
        while j < n:
            if res[j] is None:
                l[j] -= 1
                if l[j] < 0:
                    return False
            j += 1
        return True

    ilist = {1}
    res = [None] * n
    cur = n

    while ilist and (sum(l) != 0 or sum(r) != 0):
        ilist = set()
        for i in range(n):
            if l[i] == r[i] == 0 and res[i] is None:
                res[i] = cur
                ilist.add(i)
        for i in ilist:
            check = update(l, r, i, res)
            if not check:
                return False
        cur -= 1

    if not ilist:
        return False
    for i in range(n):
        if res[i] is None:
            res[i] = cur
    return res


if __name__ == '__main__':
    # 举例：调用 main(5) 运行一次
    n = 5
    res = main(n)
    if not res:
        print('NO')
    else:
        print('YES')
        for x in res:
            print(x, end=' ')