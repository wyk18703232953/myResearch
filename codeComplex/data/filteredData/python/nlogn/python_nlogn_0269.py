import random

def res(d, N):
    for i in range(1, N):
        if d[i][1] <= d[i - 1][1]:
            return str(d[i][2] + 1) + ' ' + str(d[i - 1][2] + 1)
    return '-1 -1'

def main(n):
    # 生成规模为 n 的测试数据 (a, b 为随机整数)
    d = []
    for i in range(n):
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        d.append((a, b, i))

    d = sorted(d, key=lambda x: (x[0], -x[1]))
    ans = res(d, n)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)