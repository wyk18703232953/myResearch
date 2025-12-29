import random

def interact(a, b, c, d):
    return max(min((a ^ c) - (b ^ d), 1), -1)

def main(n):
    # 生成测试数据：在 [0, 2^n) 范围内随机生成 a, b
    # 若 n > 30，为了不越界原算法位数，限制在 2^30 内
    bits = min(n, 30)
    upper = 1 << bits
    a = random.randrange(upper)
    b = random.randrange(upper)

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
                curA ^= (1 << i)
            else:
                curB ^= (1 << i)
            relative = q1
        elif q2 == 1:
            curA ^= (1 << i)
            curB ^= (1 << i)

    # 返回生成的真实 (a, b) 以及算法推测得到的 (curA, curB)
    return a, b, curA, curB

# 示例：调用 main(10)，不含任何 input()
if __name__ == "__main__":
    a, b, curA, curB = main(10)
    print("true a, b:", a, b)
    print("est  a, b:", curA, curB)