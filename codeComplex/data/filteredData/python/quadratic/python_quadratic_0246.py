import random

def main(n):
    # 随机生成满足题意的 a, b
    # 约束：min(a, b) <= 1 且 1 <= a, b <= n
    if n <= 0:
        return

    while True:
        a = random.randint(1, n)
        b = random.randint(1, n)
        if min(a, b) <= 1:
            break

    # 从这里开始是原逻辑，去掉了 input()，使用 n, a, b
    if min(a, b) > 1:
        print('NO')
        return

    m = max(a, b)

    if m == 1:
        if n == 1:
            print('YES')
            print(0)
            return
        elif n < 4:
            print('NO')
            return
        else:
            print('YES')
            for row in range(n):
                line = ['0'] * n
                if row > 0:
                    line[row - 1] = '1'
                if row < n - 1:
                    line[row + 1] = '1'
                print(''.join(line))
        return

    print('YES')

    if a == 1:
        c = '1'
        d = '0'
    else:
        c = '0'
        d = '1'

    for row in range(n):
        if row < m - 1:
            line = [c] * n
        else:
            line = [c] * (m - 1) + [d] * (n - m + 1)
        line[row] = '0'
        print(''.join(line))