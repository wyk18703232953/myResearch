import random

def main(n):
    # 生成一棵 n 个结点的随机树（结点编号 1..n）
    fst = [0 for _ in range(2 * n + 1)]
    nxt = [0 for _ in range(2 * n + 1)]
    lst = [0 for _ in range(2 * n + 1)]
    des = [0 for _ in range(2 * n + 1)]
    cnt = 0

    def add(u, v):
        nonlocal cnt
        cnt += 1
        if fst[u] == 0:
            fst[u] = cnt
        else:
            nxt[lst[u]] = cnt
        lst[u], des[cnt] = cnt, v

    # 随机生成一棵树：从 2 到 n，每个点连接到 [1..i-1] 中的随机一个
    for i in range(2, n + 1):
        p = random.randint(1, i - 1)
        add(p, i)
        add(i, p)

    # 生成一个 a 序列，可以是 1..n 的随机排列
    a = list(range(1, n + 1))
    random.shuffle(a)

    # 以下为原逻辑
    deep = [0 for _ in range(n + 1)]
    deep[1] = 1
    now, res = 1, 1
    Ans = 0

    for i in range(n):
        if deep[a[i]] == 0:
            Ans = 1
            break
        elif deep[a[i]] < now:
            Ans = 1
            break
        else:
            b = fst[a[i]]
            res += 1
            while b > 0:
                if deep[des[b]] == 0:
                    deep[des[b]] = res
                b = nxt[b]
            now = deep[a[i]]

    if Ans == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # 示例调用：n = 10，可根据需要修改
    main(10)