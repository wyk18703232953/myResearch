import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 1~1000 之间的随机整数
    l = [random.randint(1, 1000) for _ in range(n)]

    to = l.index(max(l))
    ok = 1
    for i in range(1, to):
        if l[i] <= l[i - 1]:
            ok = 0
            break
    for i in range(to + 1, n):
        if l[i] >= l[i - 1]:
            ok = 0
            break
    if ok:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)