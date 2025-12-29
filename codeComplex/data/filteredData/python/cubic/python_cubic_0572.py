import random

def gmax(hx):
    s = list(hx)
    res = []
    for i in range(9, -1, -1):
        while s[i] > 0:
            res.append(i)
            s[i] -= 1
    return res

def gmin(hx):
    s = list(hx)
    res = []
    for i in range(10):
        while s[i] > 0:
            res.append(i)
            s[i] -= 1
    return res

def main(n):
    # 1. 生成测试数据 a, b
    # a 为长度 n 的数字串（每位 0-9）
    # b 为长度在 [1, n+2] 的数字串（每位 0-9），尽量常见情况长度相近
    a = [random.randint(0, 9) for _ in range(n)]
    len_b = random.randint(1, n + 2)
    b = [random.randint(0, 9) for _ in range(len_b)]

    # 2. 按原逻辑处理
    a.sort(reverse=True)
    h = [0 for _ in range(10)]
    for x in a:
        h[x] += 1

    if len(a) < len(b):
        print(''.join(map(str, a)))
        return

    res = []

    def finalize(x):
        # 使用外层作用域的 h, res
        for y in range(x - 1, -1, -1):
            if h[y] > 0:
                res.append(y)
                h[y] -= 1
                for i in range(9, -1, -1):
                    while h[i] > 0:
                        res.append(i)
                        h[i] -= 1
                return

    p = 0
    while p < len(a) and p < len(b):
        x = b[p]
        if h[x] > 0:
            hh = list(h)
            hh[x] -= 1
            # 为避免 p+1 超界，按 b 剩余部分切片
            if b[p + 1:] >= gmin(hh):
                res.append(x)
                h[x] -= 1
            else:
                finalize(x)
                break
        else:
            finalize(x)
            break
        p += 1

    # 若循环完整跑完且没 finalize，也可能需要把剩余数字补上
    if len(res) < len(a):
        # 剩余的 h 全部从大到小填充
        for i in range(9, -1, -1):
            while h[i] > 0:
                res.append(i)
                h[i] -= 1

    print(''.join(map(str, res)))


if __name__ == "__main__":
    # 示例：n = 10
    main(10)