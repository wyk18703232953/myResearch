import random

def main(n):
    # 生成测试数据：随机选择 q，并为每个查询生成 (v, s)
    # 这里令 q 与 n 同阶，可按需求调整
    q = max(1, n)  # 至少一个查询
    queries = []

    for _ in range(q):
        # v: 1..n 之间的随机整数
        v = random.randint(1, max(1, n))
        # s: 随机步数，长度可按需求调整，这里取 0..(top+2) 之间
        if n == 1:
            s = ""  # n == 1 时，原逻辑中直接 continue，s 不起作用
        else:
            top = len(bin(n >> 1)) - 2
            length = random.randint(0, max(0, top + 2))
            s = ''.join(random.choice('ULR') for _ in range(length))
        queries.append((v, s))

    # 以下是原逻辑移植（去除 input），使用生成的测试数据
    top = len(bin(n >> 1)) - 2 if n > 1 else 0
    ans = [1] * q

    for i in range(q):
        v, s = queries[i]
        if n == 1:
            continue

        # 找到 v 从低位开始的第一个 1 所在位 h
        for h in range(top + 1):
            if v & (1 << h):
                break

        for c in s:
            if (h == top and c == 'U') or (h == 0 and c != 'U'):
                continue
            if c == 'U':
                v -= 1 << h
                h += 1
                v |= 1 << h
            elif c == 'L':
                v -= 1 << h
                h -= 1
                v |= 1 << h
            else:  # 'R'
                h -= 1
                v |= 1 << h

        ans[i] = v

    # 输出结果
    for x in ans:
        print(x)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)