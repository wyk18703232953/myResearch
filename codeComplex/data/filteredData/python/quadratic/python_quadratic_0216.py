import random

def main(n: int):
    # 根据规模 n 生成一个 r x c 的 0/1 矩阵作为测试数据
    # 这里简单设定 r = c = n，元素随机为 '0' 或 '1'
    r = n
    c = n
    a = []
    for _ in range(r):
        row = ''.join(str(random.randint(0, 1)) for _ in range(c))
        a.append(row)

    # 以下为原逻辑，无 input()
    pre = [[0 for _ in range(c)] for _ in range(r)]
    suf = [[0 for _ in range(c)] for _ in range(r)]

    for j in range(c):
        pre[0][j] = int(a[0][j])
        suf[r - 1][j] = int(a[r - 1][j])

    for i in range(1, r):
        for j in range(c):
            pre[i][j] = pre[i - 1][j] + int(a[i][j])

    for i in range(r - 2, -1, -1):
        for j in range(c):
            suf[i][j] = suf[i + 1][j] + int(a[i][j])

    ans = 'NO'
    for i in range(r):
        ok = True
        for j in range(c):
            up = pre[i - 1][j] if i - 1 >= 0 else 0
            down = suf[i + 1][j] if i + 1 < r else 0
            if up + down == 0:
                ok = False
                break
        if ok:
            ans = "YES"
            break

    print(ans)


if __name__ == "__main__":
    # 示例：用 n = 5 运行一次
    main(5)