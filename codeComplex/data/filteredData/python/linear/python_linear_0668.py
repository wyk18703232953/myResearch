import random

def main(n: int):
    # 生成测试数据
    # l: n 个正整数（原代码中有乘 2，因此这里直接生成偶数，逻辑一致且简单）
    l = [random.randint(1, 10) * 2 for _ in range(n)]
    # t: n 个操作字符 'G', 'W', 'L'
    ops = ['G', 'W', 'L']
    t_chars = [random.choice(ops) for _ in range(n)]

    # 将字符映射为 0,1,2（G -> 0, W -> 1, L -> 2）
    t = [ "GWL".index(ch) for ch in t_chars ]

    # 以下为原始逻辑（将 raw_input/input 替换为上述生成的数据）

    mins = [0 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if t[i] != 2:
            mins[i] = max(mins[i + 1] - l[i], 0)
        else:
            mins[i] = mins[i + 1] + l[i]

    curs = ans = st = 0
    for i in range(0, n):
        if t[i] == 0:  # G
            curs += l[i]
            ans += l[i] * 5
            if curs > mins[i + 1]:
                ol = (curs - mins[i + 1]) // 2
                ol = min(ol, l[i])
                ans -= 4 * ol
                curs -= 2 * ol
        if t[i] == 1:  # W
            st = 1
            curs += l[i]
            ans += l[i] * 3
        if t[i] == 2:  # L
            if curs < l[i]:
                ol = l[i] - curs
                curs = l[i]
                ans += ol * (3 if st else 5)
            curs -= l[i]
            ans += l[i]

    if curs > 0:
        ans -= curs // 2 * 2

    print(ans // 2)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)