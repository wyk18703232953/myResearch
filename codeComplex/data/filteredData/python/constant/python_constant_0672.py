import random

def ask(a, b, hidden_x, hidden_y):
    # 原交互逻辑: 返回 (x - y) <= 0
    # 这里用隐藏数 x, y 来模拟
    return (hidden_x - hidden_y) <= 0

def solve(M, hidden_x, hidden_y):
    a, b = 0, 0
    less = ask(0, 0, hidden_x, hidden_y)

    for i in range(M - 1, -1, -1):
        bit = 1 << i

        if less:
            if not ask(a | bit, b | bit, hidden_x, hidden_y):
                b |= bit
                less = ask(a, b, hidden_x, hidden_y)
            elif ask(a | bit, b, hidden_x, hidden_y):
                a |= bit
                b |= bit
        else:
            if ask(a | bit, b | bit, hidden_x, hidden_y):
                a |= bit
                less = ask(a, b, hidden_x, hidden_y)
            elif ask(a | bit, b, hidden_x, hidden_y):
                a |= bit
                b |= bit

    return a, b

def main(n: int):
    # n 为规模，用来生成测试数据的位数上限 M
    M = n

    # 生成隐藏数 x, y，范围 [0, 2^M - 1]
    max_val = (1 << M) - 1
    hidden_x = random.randint(0, max_val)
    hidden_y = random.randint(0, max_val)

    # 运行算法
    a, b = solve(M, hidden_x, hidden_y)

    # 输出结果和测试数据，方便验证
    print("hidden_x =", hidden_x)
    print("hidden_y =", hidden_y)
    print("result a =", a)
    print("result b =", b)
    print("x - y      =", hidden_x - hidden_y)
    print("a - b      =", a - b)

if __name__ == '__main__':
    # 示例：调用 main(30)
    main(30)