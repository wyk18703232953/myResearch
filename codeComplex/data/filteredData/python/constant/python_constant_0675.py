import random

def interact(a, b, c, d):
    # 原交互函数: return max(min((a ^ c) - (b ^ d), 1), -1)
    return max(min((a ^ c) - (b ^ d), 1), -1)

def solve(a, b):
    def ask(c, d):
        return interact(a, b, c, d)

    relative = ask(0, 0)
    curA = 0
    curB = 0

    for i in range(29, -1, -1):
        q1 = ask(curA ^ (1 << i), curB)
        q2 = ask(curA, curB ^ (1 << i))

        if q1 == q2:
            if relative == 1:
                curA ^= 1 << i
            else:
                curB ^= 1 << i
            relative = q1
        elif q2 == 1:
            curA ^= 1 << i
            curB ^= 1 << i
    return curA, curB

def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设 a, b 为 [0, 2^n) 范围内的随机非负整数，n 不超过 30
    n = min(n, 30)
    max_val = 1 << n
    a = random.randrange(max_val)
    b = random.randrange(max_val)

    curA, curB = solve(a, b)
    return {
        "a": a,
        "b": b,
        "recovered_a": curA,
        "recovered_b": curB,
        "correct": (a == curA and b == curB)
    }

if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    result = main(10)
    print(result)