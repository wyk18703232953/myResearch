import random

def ask_factory(secret_a, secret_b):
    """
    返回一个闭包 ask(a, b)，模拟交互：
    原始逻辑是：print("?", a, b)，然后读一个整数并判断 <= 0。
    通常这类交互题中，返回的是比较结果：sign((a - secret_a) - (b - secret_b))
    这里我们用 (a - b) 与 (secret_a - secret_b) 的大小关系来模拟：
    若 (a - b) <= (secret_a - secret_b) 则返回 True，否则返回 False
    """
    target = secret_a - secret_b

    def ask(a, b):
        return (a - b) <= target

    return ask


def solve(M, ask):
    a, b = 0, 0
    less = ask(0, 0)

    for i in range(M - 1, -1, -1):
        bit = 1 << i

        if less:
            if not ask(a | bit, b | bit):
                b |= bit
                less = ask(a, b)
            elif ask(a | bit, b):
                a |= bit
                b |= bit
        else:
            if ask(a | bit, b | bit):
                a |= bit
                less = ask(a, b)
            elif ask(a | bit, b):
                a |= bit
                b |= bit

    return a, b


def main(n: int):
    """
    n: 规模，用作位数上界；即我们会在 [0, 2^n) 范围内随机生成 secret_a, secret_b。
    """
    # 生成测试数据
    max_val = 1 << n
    secret_a = random.randrange(max_val)
    secret_b = random.randrange(max_val)

    # 构造交互接口
    ask = ask_factory(secret_a, secret_b)

    # 执行原逻辑
    a, b = solve(n, ask)

    # 输出结果（包括真实值与推断值，便于测试）
    print("secret_a:", secret_a)
    print("secret_b:", secret_b)
    print("found_a: ", a)
    print("found_b: ", b)


if __name__ == '__main__':
    # 示例运行：位长 30
    main(30)