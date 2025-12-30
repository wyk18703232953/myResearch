import random
import string

def rotate(s, n):
    ret = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[i][j] = s[j][n - 1 - i]
    return ret

def v_mirror(s):
    return list(reversed(s))

def h_mirror(s):
    return [list(reversed(row)) for row in s]

def solve(s1, s2, n):
    cur = [row[:] for row in s1]
    for _ in range(4):
        if cur == s2:
            return True
        if v_mirror(cur) == s2:
            return True
        if h_mirror(cur) == s2:
            return True
        if v_mirror(h_mirror(cur)) == s2:
            return True
        cur = rotate(cur, n)
    return False

def gen_random_grid(n):
    # 使用两种字符生成随机方阵，便于观察
    chars = ['.', '#']
    return [[random.choice(chars) for _ in range(n)] for _ in range(n)]

def main(n):
    # 生成测试数据：随机方阵 s1 和 s2
    s1 = gen_random_grid(n)

    # 随机决定是否让 s2 与 s1 存在合法变换关系
    make_related = random.choice([True, False])
    if make_related:
        # 从 s1 通过一系列随机变换生成 s2
        s2 = [row[:] for row in s1]
        # 随机旋转 0~3 次
        k = random.randint(0, 3)
        for _ in range(k):
            s2 = rotate(s2, n)
        # 随机选择是否做镜像操作
        if random.choice([True, False]):
            s2 = v_mirror(s2)
        if random.choice([True, False]):
            s2 = h_mirror(s2)
    else:
        # 完全随机生成 s2，通常与 s1 不存在合法变换关系
        s2 = gen_random_grid(n)

    result = solve(s1, s2, n)
    print('Yes' if result else 'No')

if __name__ == "__main__":
    # 示例：规模为 5，可按需修改
    main(5)