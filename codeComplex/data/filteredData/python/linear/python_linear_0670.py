import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 1 到 10^6 之间的随机整数
    a = [random.randint(1, 10**6) for _ in range(n)]

    q = (10 ** 6) * [-1]
    pnt = -1
    ans = "YES"
    for i in range(n):
        if pnt == -1:
            pnt += 1
            q[pnt] = a[i]
        else:
            if q[pnt] == a[i] or abs(q[pnt] - a[i]) % 2 == 0:
                q[pnt] = -1
                pnt -= 1
            else:
                pnt += 1
                q[pnt] = a[i]
    if pnt > 0:
        ans = "NO"
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)