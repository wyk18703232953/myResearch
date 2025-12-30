import random

def main(n):
    # n 用来控制规模：行数 s 和列数 l，简单设定为 s = n, l = n
    s = n
    l = n

    sig = []
    utp = []

    if s == 0 or l == 0:
        print('NO')
        return

    # 生成测试数据：s 行，每行 l 位 0/1
    for _ in range(s):
        # 原程序用 list(map(int, input()))，等价于逐字符读取 0/1
        row = [random.randint(0, 1) for _ in range(l)]
        sig.append(row)

    # 计算每一列的和 utp
    for i in range(l):
        out = 0
        for x in range(s):
            out += sig[x][i]
        utp.append(out)

    # 按行和排序
    sig = sorted(sig, key=sum)

    # 检查是否存在一行，使得对每一列 utp[x] - sig[i][x] > 0
    for i in range(s):
        res1 = 0
        for x in range(l):
            if utp[x] - sig[i][x] <= 0:
                break
            else:
                res1 += 1
        if res1 == l:
            print('YES')
            return

    print('NO')


if __name__ == "__main__":
    # 示例调用：可以修改 n 测试规模
    main(5)