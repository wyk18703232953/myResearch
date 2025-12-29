import random

def main(n):
    # 生成测试数据：k 在 [1, min(20, n)]，a 为长度 n 的数组，元素在 [0, 255]
    k = random.randint(1, min(20, n if n > 0 else 1))
    a = [random.randint(0, 255) for _ in range(max(0, n))]

    p = [-1] * 256
    p[0] = 0

    for x in a:
        if p[x] < 0:
            for y in range(x - 1, max(-1, x - k), -1):
                if p[y] >= 0:
                    if p[y] + k > x:
                        p[x] = p[y]
                    else:
                        p[x] = p[y + 1] = y + 1
                    break
            if p[x] < 0:
                p[x] = p[x - k + 1] = x - k + 1

    b = [p[x] for x in a]
    print(' '.join(map(str, b)))