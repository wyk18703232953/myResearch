import random

def l(a, e):
    b = bin(a)[2:]
    b = "0" * (e - len(b)) + b
    d = len(b)
    c = 0
    for i in range(d - 1, -1, -1):
        if b[i] == "1":
            c = d - 1 - i
            break
    if c == 0:
        return -1
    return a - 2 ** (c - 1)

def r(a, e):
    b = bin(a)[2:]
    b = "0" * (e - len(b)) + b
    d = len(b)
    c = 0
    for i in range(d - 1, -1, -1):
        if b[i] == "1":
            c = d - 1 - i
            break
    if c == 0:
        return -1
    return a + 2 ** (c - 1)

def u(a, e):
    b = bin(a)[2:]
    b = "0" * (e - len(b)) + b
    d = len(b)
    c = 0
    for i in range(d - 1, -1, -1):
        if b[i] == "1":
            c = d - 1 - i
            break
    if c == d - 1:
        return -1
    else:
        if b[d - 1 - c - 1] == "0":
            return a + (2 ** c)
        else:
            return a - (2 ** c)

def main(n):
    # 根据规模 n 生成测试数据
    # n: 用作原程序中的 n，节点上界
    # q: 查询次数，这里设为与 n 同数量级
    if n <= 0:
        return

    q = max(1, n)  # 至少 1 次查询
    e = len(bin(n)[2:])

    # 随机生成 q 组 (a, 操作串)
    # a 在 [1, n] 范围内
    # 操作串长度在 [1, e] 之间，每个字符是 'L','R','U'
    ops = ['L', 'R', 'U']

    for _ in range(q):
        a = random.randint(1, n)
        length = random.randint(1, e)
        b = ''.join(random.choice(ops) for _ in range(length))

        # 模拟原逻辑
        for ch in b:
            if ch == "U":
                c = u(a, e)
                if c != -1:
                    a = c
            elif ch == "R":
                c = r(a, e)
                if c != -1:
                    a = c
            elif ch == "L":
                c = l(a, e)
                if c != -1:
                    a = c

        print(a)

if __name__ == "__main__":
    # 示例：可在此处调用 main 进行测试
    main(10)