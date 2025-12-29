import random

def lvl(val):
    tot = 1
    curr = -1
    while val % tot == 0:
        curr += 1
        tot *= 2
    return [curr, val * 2 // tot, tot // 2]

def main(n):
    # 生成测试数据
    # 这里生成 q 个查询，每个查询包含一个初始节点 curr 和一串操作 s
    # 可根据需要修改测试数据规模与生成方式
    q = min(n, 10)  # 示例：最多生成 10 个查询
    queries = []
    for _ in range(q):
        curr = random.randint(1, n)
        length_s = random.randint(1, 10)
        ops = ['U', 'L', 'R']
        s = ''.join(random.choice(ops) for _ in range(length_s))
        queries.append((curr, s))

    # 原逻辑
    results = []
    for curr, s in queries:
        l, v, pw = lvl(curr)
        for j in s:
            if j == "U":
                if v % 4 == 3:
                    curr = curr - pw
                else:
                    if curr + pw <= n:
                        curr = curr + pw
            elif j == "R":
                if l > 0:
                    curr = curr + pw // 2
            elif j == "L":
                if l > 0:
                    curr = curr - pw // 2
            l, v, pw = lvl(curr)
        results.append(curr)

    # 输出结果
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此处调整
    main(2**20 - 1)