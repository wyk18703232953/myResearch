import random

def solve(n, p, s):
    p.append((0, 0))
    p.sort()
    t = 0
    while p:
        x = p.pop()
        s, t = x[0], max(x[1], t + abs(s - x[0]))
    return t

def main(n):
    # 生成规模为 n 的测试数据
    # 坐标和时间均生成在可控范围内，可根据需要调整
    max_coord = 10**6
    max_time = 10**6

    # 起始位置 s
    s = random.randint(-max_coord, max_coord)

    # 生成 n 个点 (位置, 时间)
    p = []
    for _ in range(n):
        pos = random.randint(-max_coord, max_coord)
        tim = random.randint(0, max_time)
        p.append((pos, tim))

    # 调用原逻辑
    ans = solve(n, p, s)
    print(ans)

if __name__ == "__main__":
    # 示例：运行时可在此处修改 n 的默认值
    main(5)