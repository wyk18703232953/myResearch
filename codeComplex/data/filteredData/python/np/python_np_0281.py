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
    if b[d - 1 - c - 1] == "0":
        return a + 2 ** c
    return a - 2 ** c


def main(n):
    if n < 1:
        return
    # 输入结构：n, q; 然后 q 组 (a, b)
    # 这里将 n 作为“位数规模”，根据 n 派生:
    #   - 树最大节点值 N = 2^n - 1
    #   - 查询数 q = n
    #   - 每个查询的初始节点 a 按 1..q 映射到 [1, N]
    #   - 每个操作串长度也与 n 相关且确定
    N = (1 << n) - 1
    q = n
    e = len(bin(N)[2:])

    results = []
    for qi in range(q):
        # a 在 1..N 内循环分布
        a = (qi % N) + 1

        # 构造确定性的操作串 b
        # 规则示例：对每个位置 j，根据 (qi+j) 的模值在 'U','L','R' 中选择
        ops = []
        length = n + qi  # 随查询线性增长，利于规模化
        for j in range(length):
            t = (qi + j) % 3
            if t == 0:
                ops.append("U")
            elif t == 1:
                ops.append("L")
            else:
                ops.append("R")
        b = "".join(ops)

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
        results.append(a)

    # 为了保持原程序的输出行为，这里将所有结果按行打印
    for value in results:
        print(value)


if __name__ == "__main__":
    # 示例：使用 n=5 进行一次确定性运行
    main(5)