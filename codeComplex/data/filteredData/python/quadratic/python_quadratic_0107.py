import random
import string

def rotate_90(a):
    b = []
    for x in range(len(a)):
        l = []
        for y in range(len(a) - 1, -1, -1):
            l.append(a[y][x])
        b.append(l)
    return b

def flip(a):
    b = []
    for x in range(len(a)):
        l = []
        for y in range(len(a) - 1, -1, -1):
            l.append(a[x][y])
        b.append(l)
    return b

def generate_random_matrix(n):
    # 生成 n×n 的随机字符矩阵（字符从小写字母中选择）
    mat = []
    for _ in range(n):
        row = [random.choice(string.ascii_lowercase) for _ in range(n)]
        mat.append(row)
    return mat

def choose_transformation(mat):
    # 随机选择是否对 mat 做合法变换得到目标矩阵
    # 返回 (源矩阵, 目标矩阵, 期望结果 'yes'/'no')
    should_match = random.choice([True, False])

    if not should_match:
        # 尝试生成一个与所有变换结果都不同的矩阵
        target = generate_random_matrix(len(mat))
        # 理论上仍有极小概率随机等于某个变换结果，这里不做额外排除
        return mat, target, 'no'

    # 按题目变换方式生成匹配矩阵
    transformed = [row[:] for row in mat]
    # 先随机选择是否翻转
    if random.choice([True, False]):
        transformed = flip(transformed)
        # 此时只允许再旋转 0~3 次
        k = random.randint(0, 3)
    else:
        # 不翻转，只旋转 1~4 次（与原逻辑匹配：先旋转再比较）
        k = random.randint(1, 4)

    for _ in range(k):
        transformed = rotate_90(transformed)

    return mat, transformed, 'yes'

def check_equivalent(l, l2):
    d = 'no'
    # 与原程序保持一致的逻辑
    for _ in range(4):
        l = rotate_90(l)
        if l == l2:
            d = 'yes'
    l = flip(l)
    for _ in range(4):
        l = rotate_90(l)
        if l == l2:
            d = 'yes'
    return d

def main(n):
    # 生成测试数据
    src = generate_random_matrix(n)
    src, target, expected = choose_transformation(src)

    # 调用原逻辑判断
    result = check_equivalent([row[:] for row in src], [row[:] for row in target])

    # 输出与原程序一致的最终判断结果
    print(result)

if __name__ == "__main__":
    # 示例运行：规模为 4
    main(4)