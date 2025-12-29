from itertools import chain, combinations, permutations
import random
import string


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, r) for r in range(len(xs) + 1))


def copy_matrix(m):
    n = len(m)
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[i][j])
        res.append(row)
    return res


def rot90(m):
    # rotate 90 degrees clockwise
    n = len(m)
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[n - 1 - j][i])
        res.append(row)
    return res


def vert(m):
    # reverse rows order (flip vertically)
    n = len(m)
    res = []
    for i in range(n):
        res.append(m[i][::-1])
    return res


def gor(m):
    # reverse columns order (flip horizontally)
    n = len(m)
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[i][n - 1 - j])
        res.append(row)
    return res


def generate_random_matrix(n):
    # 使用 '0' 和 '1' 生成测试数据，也可以改成其他字符集
    chars = "01"
    mat = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.choice(chars))
        mat.append(row)
    return mat


def apply_random_transforms(mat):
    # 随机选择若干种变换并随机排列后应用，生成 cl2
    transforms = [rot90, rot90, rot90, vert, gor]
    # powerset 返回所有子集，我们随机选一个子集，然后随机排列其元素
    subset = random.choice(list(powerset(transforms)))
    perm = random.sample(subset, len(subset)) if subset else []
    res = copy_matrix(mat)
    for f in perm:
        res = f(res)
    return res


def solve(cl1, cl2):
    # 原逻辑封装成函数，判断是否可以通过若干变换从 cl1 得到 cl2
    cm = [rot90, rot90, rot90, vert, gor]
    cm = list(powerset(cm))
    if cl1 == cl2:
        return True
    for x in cm:
        for y in permutations(x):
            t = copy_matrix(cl1)
            for z in y:
                t = z(t)
            if t == cl2:
                return True
    return False


def main(n):
    # 1. 生成测试数据 cl1
    cl1 = generate_random_matrix(n)
    # 2. 基于 cl1 生成 cl2（通过随机若干次合法变换）
    cl2 = apply_random_transforms(cl1)
    # 3. 运行原逻辑判断并输出结果
    res = solve(cl1, cl2)
    if res:
        print("Yes")
    else:
        print("No")