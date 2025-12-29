import random

def main(n):
    # 生成测试数据：n 和 x，以及长度为 n 的数组 arr
    # 可根据需要调整生成策略
    x = random.randint(0, 2 * n)
    arr = [random.randint(0, 2 * n) for _ in range(n)]

    MAXV = 100100
    f = [0] * MAXV
    s = [0] * MAXV
    can = [False] * MAXV

    for i in range(n):
        v = arr[i]
        if v < MAXV:
            f[v] += 1
        vx = v & x
        if vx < MAXV:
            s[vx] += 1
            if vx != v:
                can[vx] = True

    ans = 3
    for i in range(MAXV):
        if f[i] >= 2:
            ans = 0
            break
        if f[i] == 1 and s[i] >= 1:
            if can[i]:
                ans = min(ans, 1)
        if s[i] >= 2:
            ans = min(ans, 2)

    if ans == 3:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)