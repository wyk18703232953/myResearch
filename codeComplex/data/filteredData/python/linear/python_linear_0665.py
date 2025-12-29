import random

def main(n: int):
    # 生成测试数据：
    # l：长度为 n 的正整数数组
    # t：长度为 n 的字符串，由 'G', 'W', 'L' 组成
    # 可按需要修改数据分布
    random.seed(0)
    l = [random.randint(1, 10) for _ in range(n)]
    choices = ['G', 'W', 'L']
    t_str = ''.join(random.choice(choices) for _ in range(n))

    # 将原始逻辑中的输入替换为上述生成的数据
    # l: 原程序中乘 2 的数组
    l = [x * 2 for x in l]
    t = [ "GWL".index(ch) for ch in t_str ]

    mins = [0 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if t[i] != 2:
            mins[i] = max(mins[i + 1] - l[i], 0)
        else:
            mins[i] = mins[i + 1] + l[i]

    curs = ans = st = 0
    for i in range(n):
        if t[i] == 0:
            curs += l[i]
            ans += l[i] * 5
            if curs > mins[i + 1]:
                ol = (curs - mins[i + 1]) // 2
                ol = min(ol, l[i])
                ans -= 4 * ol
                curs -= 2 * ol
        if t[i] == 1:
            st = 1
            curs += l[i]
            ans += l[i] * 3
        if t[i] == 2:
            if curs < l[i]:
                ol = l[i] - curs
                curs = l[i]
                ans += ol * (3 if st else 5)
            curs -= l[i]
            ans += l[i]
    if curs > 0:
        ans -= (curs // 2) * 2

    result = ans // 2
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用
    main(10)