import random
import string


def rotate(L, n):
    # rotate 90 degrees clockwise
    L1 = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            L1[n - j - 1] += L[i][j]
    return L1


def flip_v(L, n):
    # flip vertically (left-right)
    L1 = []
    for i in range(n):
        L1.append(L[i][::-1])
    return L1


def flip_h(L, n):
    # flip horizontally (top-bottom)
    L1 = []
    for i in range(n):
        L1.append(L[n - i - 1])
    return L1


def generate_random_grid(n):
    # generate an n x n grid of random uppercase letters
    letters = string.ascii_uppercase
    return [''.join(random.choice(letters) for _ in range(n)) for _ in range(n)]


def main(n):
    # 生成测试数据：随机方阵 L 和由 L 做一次随机变换得到的 M（保证有时输出 Yes）
    L = generate_random_grid(n)

    # 随机选择一种变换生成 M，或直接复制 L
    transforms = [
        lambda x: x,                       # 原图
        lambda x: rotate(x, n),            # 旋转 90
        lambda x: rotate(rotate(x, n), n), # 旋转 180
        lambda x: rotate(rotate(rotate(x, n), n), n),  # 旋转 270
        lambda x: flip_v(x, n),            # 垂直翻转
        lambda x: flip_h(x, n),            # 水平翻转
        lambda x: rotate(flip_v(x, n), n),
        lambda x: rotate(rotate(flip_v(x, n), n), n),
        lambda x: rotate(rotate(rotate(flip_v(x, n), n), n), n),
        lambda x: rotate(flip_h(x, n), n),
        lambda x: rotate(rotate(flip_h(x, n), n), n),
        lambda x: rotate(rotate(rotate(flip_h(x, n), n), n), n),
    ]
    transform = random.choice(transforms)
    M = transform(L)

    # 按原逻辑枚举所有变换并比较
    L1 = rotate(L, n)
    L2 = rotate(L1, n)
    L3 = rotate(L2, n)
    L4 = flip_v(L, n)
    L5 = flip_h(L, n)
    L6 = rotate(L4, n)
    L7 = rotate(L6, n)
    L8 = rotate(L7, n)
    L9 = rotate(L5, n)
    L10 = rotate(L9, n)
    L11 = rotate(L10, n)

    if (
        L == M
        or L1 == M
        or L2 == M
        or L3 == M
        or L4 == M
        or L5 == M
        or L6 == M
        or L7 == M
        or L8 == M
        or L9 == M
        or L10 == M
        or L11 == M
    ):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    # 示例：n=4
    main(4)