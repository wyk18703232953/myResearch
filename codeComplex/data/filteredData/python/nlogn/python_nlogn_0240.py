import random

def f(a, b, c):
    # Cross product (a->b) x (a->c)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def g(fi, se, p):
    q = []
    for x in p:
        if f(fi, se, x):
            if len(q) < 2:
                q.append(x)
            else:
                if f(q[0], q[1], x):
                    return 1
    return 0

def main(n):
    # 根据 n 生成测试数据：生成 n 个随机点
    # 可根据需要调整坐标范围
    p = [(random.randint(-10**6, 10**6), random.randint(-10**6, 10**6)) for _ in range(n)]

    # 保持原逻辑
    if n > 4 and all([
        g(p[0], p[1], p),
        g(p[0], p[2], p),
        g(p[1], p[2], p)
    ]):
        print('NO')
    else:
        print('YES')

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)